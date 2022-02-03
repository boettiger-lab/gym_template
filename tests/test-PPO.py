import gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.evaluation import evaluate_policy

import gym_template


def test_ppo():
    env = gym.make("template-v0")
    check_env(env)
    model = PPO("MlpPolicy", env, verbose=0)
    model.learn(total_timesteps=100)
    # Evaluate model
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=2)
