from gym.envs.registration import register
from gym_template.envs.base import BaseEnv
from gym_template.envs.v1 import Env1

register(
    id="template-v0",
    entry_point="gym_template.envs:BaseEnv",
)

register(
    id="template-v1",
    entry_point="gym_template.envs:Env1",
)

