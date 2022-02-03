import gym

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

