import gym
import numpy as np
from matplotlib import pyplot as plt

env = gym.make('FrozenLake-v0')

print(env.action_space.n)

print(np.random.randn(1, env.action_space.n))

linear = []
log = []

number_of_episodes = 2000

for i in range(number_of_episodes):
    linear.append(1. - (i/number_of_episodes))
    log.append(1./(i+1))


fig = plt.figure()

plot1 = fig.add_subplot(211)
plot1.plot(linear)

plot2 = fig.add_subplot(212)
plot2.plot(log)

plt.show()

