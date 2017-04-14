import gym
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# load the env
env = gym.make('Taxi-v1')

for i in range(10):
    env.reset()
    env.render()
