import gym
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# load the env
env = gym.make('FrozenLake-v0')

# the Q-netwok approach

# implement the network itself
tf.reset_default_graph()

# init feed forward nn to choose the best action
inputs1 = tf.placeholder(shape=[1, 16], dtype=tf.float32)
W = tf.Variable(tf.random_uniform([16, 4], 0, 0.01))
Qout = tf.matmul(inputs1, W)
predict = tf.argmax(Qout, 1)

# below we obtain the loss by takig the sum of the squares difference between the target and the prediction Q values.
nextQ = tf.placeholder(shape=[1, 4], dtype=tf.placeholder(shape=[1, 4], dtype=tf.float32))
loss = tf.reduce_sum(tf.square(nextQ - Qout))
trainer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
updateModel = trainer.minimize(loss)

# training the network
init = tf.initialize_all_variables()
# set learning parameters
y = .99
e = 0.1
num_episodes = 200
# create a list that containes total reqrds and steps per episode
jList = []
rList = []
with tf.Session() as sess:
    sess.run(init)
    for i in range(num_episodes):
        # reset the env and get first observation
        s = env.reset()
        rAll = 0
        d = False
        j = 0
        # the q net
        while j < 99:
            j += 1
            # choose an aciton by greedily, with chance of random actions , from the q tabe
            a, allQ = sess.run([predict, Qout], feed_dict={inputs1: np.identity(16)[s:s+1]})
            if np.random.rand(1) < e:
                a[0] = env.action_space_sample()
            # get new state and reward from env
            s1, r, d, _ = env.step(a[0])
            # obtain the q values by  feeding the new state throught our q net
            Q1 = sess.run(Qout, feed_dict={inputs1: np.identity(16)[s1:s1+1]})
            # obtain max q and set our target value for chosen action
            maxQ1 = np.max(Q1)
            targetQ = allQ
            targetQ[0,a[0]] = r + y*maxQ1
            # train our nn using target
            _,W1 = sess.run([updateModel,W],feed_dict={inputs1:np.identity(16)[s:s+1],nextQ:targetQ})
            rAll += r
            s = s1
            if d == True:
                #Reduce chance of random action as we train the model.
                e = 1./((i/50) + 10)
                break
        jList.append(j)
        rList.append(rAll)
print("Percent of successful episodes: " + str(sum(rList)/num_episodes) + "%")

