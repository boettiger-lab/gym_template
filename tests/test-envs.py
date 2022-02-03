import gym
import numpy as np
from stable_baselines3.common.env_checker import check_env


def test_template():
    env = gym.make("template-v0")
    check_env(env)


