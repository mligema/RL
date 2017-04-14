import gym
import numpy as np
env = gym.make('FrozenLake-v0')
#Initialize table with all zeros
Q = np.zeros([env.observation_space.n,env.action_space.n])
# Set learning parameters
lr = .85
y = .99
num_episodes = 10000
#create lists to contain total rewards and steps per episode
jList = []
rList = []
for i in range(num_episodes):
    #Reset environment and get first new observation
    s = env.reset()
    rAll = 0
    d = False
    j = 0
    #The Q-Table learning algorithm
    while j < 99:
        j += 1
        #Choose an action by greedily (with noise) picking from Q table

        linear_to_zero = 1. - (i/num_episodes)

        #if linear_to_zero < 0:
        #    linear_to_zero = 0

        logarithmic_to_zero = 1./(i + 1)

        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n) * linear_to_zero)
        #Get new state and reward from environment
        s1,r,d,_ = env.step(a)
        #Update Q-Table with new knowledge
        Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])
        rAll += r
        s = s1
        if d == True:
            break
    jList.append(j)
    rList.append(rAll)

print("Score over time: " + str(sum(rList)/num_episodes))
print("Score over the last 100 episodes: " + str(sum(rList[-100:])/100))
print("Final Q-Table Values")
print("          left          down          right          up")
print(Q)
print()

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

import matplotlib.pyplot as plt

fig = plt.figure()

plot1 = fig.add_subplot(211)
plot1.plot(rList)

plot2 = fig.add_subplot(212)
plot2.plot(jList)

plt.show()
