import gym
from gym.envs.registration import register
from gym_template.envs.base import BaseEnv


class Env1(BaseEnv):
    def __init__(self, env_config):
        self.action_space = gym.spaces.Discrete(6)
        self.observation_space = gym.spaces.Box(0.0, 6.0)

    def step(self, action):
        self.obs = (self.obs + 1) % 6
        reward = action
        done = False
        info = {}
        return self.obs, reward, done, info


register(
    id="template-v1",
    entry_point="gym_template.envs.v1:Env1",
)
