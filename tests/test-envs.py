import gym
import numpy as np
from gym.envs.registration import register
from stable_baselines3.common.env_checker import check_env

import gym_template


def test_template():
    env = gym.make("template-v0")
    check_env(env)
