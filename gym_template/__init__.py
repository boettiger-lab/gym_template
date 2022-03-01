from gym.envs.registration import register

register(
    id="template-v0",
    entry_point="gym_template.envs.base:BaseEnv",
)

register(
    id="template-v1",
    entry_point="gym_template.envs.v1:Env1",
)
