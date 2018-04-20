
from gym.core import Env
from gym.spaces.box import Box
import numpy as np


class MyEnvironment(Env):
    def __init__(self):
        self.action_space = Box(low=np.array([-1.]), high=np.array([1.]))
        self.observation_space = Box(low=np.array([-1.]), high=np.array([1.]))
        self.reward_range = (-1., 1.)

    def _step(self, action):
        return self.observation_space.sample()

    def _reset(self):
        pass

    def _render(self, mode='human', close=False):
        pass

    def _configure(self):
        pass

    def _seed(self, seed=None):
        pass


if __name__ == '__main__':
    import gym
    from myenv import MyEnvironment

    a = gym.make('MyEnv-v0')

