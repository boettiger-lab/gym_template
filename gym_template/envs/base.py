import gym


class BaseEnv(gym.Env):
    def __init__(self, env_config={}):
        self.action_space = gym.spaces.Discrete(6)
        self.observation_space = gym.spaces.Discrete(6)

    def step(self, action):
        self.obs = (self.obs + 1) % 6
        reward = int(action == self.obs)
        done = False
        info = {}
        return self.obs, reward, done, info

    def reset(self):
        self.obs = 1
        return self.obs
