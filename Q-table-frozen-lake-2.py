import gym
import numpy as np

env = gym.make('FrozenLake-v0')

# init table with zeros

Q = np.zeros([env.observation_space.n, env.action_space.n])

# set learning parameters
lr = .85
y = .99
num_episodes = 500000
# create lists to contain total reward and steps per episode
jList = []
rList = []

for i in range(num_episodes):

    print(i)

    # reset the env and get first new observation
    s = env.reset()
    rAll = 0
    d = False
    j = 0

    # the qtable learning algorithm
    while j < 99:
        j += 1
        # choose and aciton by greedily (with noise) picking an action from the q table
        # a = the chosen action
        #a = np.argmax(Q[s, :]) + np.random.randn(1, env.action_space.n)*(1./(i+1))
        #a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1. - (i/num_episodes)))
        # get the new state and reward from the environment
        s1, r, d, _ = env.step(a)
        # Update the qtable with new knowledge
        Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])
        rAll += r
        s = s1
        if d == True:
            break
    jList.append(j)
    rList.append(rAll)

print(sum(rList[-100:])/100)


s = env.reset()
rAll = 0
d = False
j = 0
while j < 99:
    j += 1

    a = np.argmax(Q[s,:])

    s, r, d, _ = env.step(a)
    env.render()
    if d == True:
        print('Done')
        break



