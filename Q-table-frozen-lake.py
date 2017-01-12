import gym
import numpy as np
from pprint import pprint

# load the environment
env = gym.make('FrozenLake-v0')

# in this case the obseravation space is discrete 16
observation_space = env.observation_space.n
print(observation_space)

# in this case the action space is discrete 4
action_space = env.action_space.n
print(action_space)

# based on the discrete observation space and discrete action space
# we can initialize Q-table learning table
Q = np.zeros([observation_space, action_space])

# learning parameters
learning_rate = .85
y = .99

number_of_episodes = 2000

# create a list of total rewards and steps per episode
reward_list = []
j_list = []

# present 2000 episodes of environments
for i in range(number_of_episodes):
    # reset the environment and get first new observation
    state = env.reset()
    episode_reward = 0
    done = False
    j = 0

    # The Q-Table learning algorithm
    while not done and j < 99:

        env.render()

        j += 1
        # Choose an action by greedily ( with noise ) picking from the Q table from the state you are in.
        actions_available_in_state_s = Q[state, :]
        print('actions_available_in_state_s ', actions_available_in_state_s)
        nr_halving_every_iteration = 1./(i + 1)
        print('nr_halving_every_iteration ', nr_halving_every_iteration)
        current_action_space = env.action_space.n
        print('current_action_space ', current_action_space)
        random_floats = np.random.randn(1, current_action_space)
        print('random_floats', random_floats)
        rand_floats_times_halfing_every_iteration = random_floats * nr_halving_every_iteration
        wat = actions_available_in_state_s + rand_floats_times_halfing_every_iteration
        print('wat? ', wat)
        print('wat max', np.amax(wat))
        best_action_in_this_state = np.argmax(wat)
        print('which it was ? ', best_action_in_this_state)


        #action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) * (1./(i + 1)))

        # after having chosen the best action DO/Execute that action and observe the environment

        next_state, reward, done, info = env.step(best_action_in_this_state)

        # Now update the Qtable in the place you are right now

        Q[state, best_action_in_this_state] = Q[state, best_action_in_this_state] + learning_rate * (reward + y * np.max(Q[next_state, :]) - Q[state, best_action_in_this_state])

        episode_reward += reward

        state = next_state

        #if done == True:
        #    break

    j_list.append(j)
    reward_list.append(episode_reward)

print("Final Q-Table Values")
print("          left          down          right          up")
print(Q)
print(j_list)
print(reward_list)

import matplotlib.pyplot as plt

plt.plot(Q, 'ro')
plt.show()

