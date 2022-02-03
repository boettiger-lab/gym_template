[![Install & Test](https://github.com/boettiger-lab/gym_template/workflows/Install%20&%20Train/badge.svg)](https://github.com/boettiger-lab/gym_template/runs/1323937050?check_suite_focus=true)

<!--
[![PyPI Version](https://img.shields.io/pypi/v/gym_template)](https://pypi.org/project/gym_template/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/gym_template)
[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
-->

The [OpenAI gym](https://github.com/openai/gym) specification provides a widely recognized standard API for specifying sequential decision problems (PO)MDPs ([Brockman et al](https://arxiv.org/pdf/1606.01540)) which is compatible with most leading RL frameworks.
A minimal `gym` object is a Python class with at least three core methods: `init`, `reset`, and `step`, like so:

```python

class MyEnv(gym.Env):
    def __init__(self, env_config):
        self.action_space = <gym.Space>
        self.observation_space = <gym.Space>
    def reset(self):
        return <obs>
    def step(self, action):
        return <obs>, <reward: float>, <done: bool>, <info: dict>
```

In practice, gyms will often define different versions of the class corresponding to alternate and often more complex variations of the same objective.
Class inheritance comes in handy in such cases. 
In principle it is possible to allow alternative configurations (i.e. alternative parameter values) for a given gym through the `env_config` dictionary in the `init` method, but in practice methods are usually benchmarked against the default configuration, so choose these carefully.  
A minimally functional example showing two versions, class inheritence, and 'registering' of the gym are included here.
More information can be found in the [gym](https://github.com/openai/gym) repository (including its extensive collection of gyms included there-in) and by examining other existing gyms.




Tasks to deploy template:

## Inital steps

- [] Update `setup.py` metadata
- [] Rename `gym_template` directory to match your module name
- [] Update module name in `Makefile`
- [] Update tests to reflect module name.

## Building the gym

- [] Edit the methods and class definitions in renamed `gym_template` directory to define the core gym methods.



# Infrastructure already provided:

This template includes automatic linting and testing using GitHub Actions and a Makefile for automating common tasks:

- `make check-codestyle` Check code style conforms to [`black`](https://github.com/psf/black) code formatter (with 79 char soft character limit per line). (see `format` below to auto-reformat valid code)
- `make format` Auto-reformats code using `isort` (imports) and `black`.
- `make type` runs [`pytype`](https://github.com/google/pytype) to check Python classes.
- `make lint` runs [`flake8`](https://flake8.pycqa.org/en/latest/) to check for syntax errors in Python code
- `make commit-checks`: runs make calls for `format`, `type`, and `lint`.  (Ideally should be run before any git commit)
- `make install` installs the python module
- `make pytest` runs pytest suite using configuration in `scripts/run_tests.sh`
- `make release`: Publish a releast to pypi.org using [`twine`](https://github.com/pypa/twine/), will ask for required credentials

- Note that additional tools for documentation via [sphinx](https://www.sphinx-doc.org/en/master/): `make spelling, `make doc`, and `make clean` are not fully flushed out here.

_Makefile automation is based on (MIT-licensed) [stable-baselines3](https://github.com/DLR-RM/stable-baselines3)_


