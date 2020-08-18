# I^2HRL

### Basic Installation

Our code is based on [h-baselines](https://github.com/AboudyKreidieh/h-baselines).

To install the h-baselines repository, begin by opening a terminal and set the
working directory of the terminal to match

```bash
cd path/to/h-baselines
```

Next, create and activate a conda environment for this repository by running 
the commands in the script below. Note that this is not required, but highly 
recommended. If you do not have Anaconda on your device, refer to the provided
links to install either [Anaconda](https://www.anaconda.com/download) or
[Miniconda](https://conda.io/miniconda.html).

```bash
conda env create -f environment.yml
source activate h-baselines
```

Finally, install the contents of the repository onto your conda environment (or
your local python build) by running the following command:

```bash
pip install -e .
```

### Installing MuJoCo

In order to run the MuJoCo environments described within the README, you
will need to install MuJoCo and the mujoco-py package. To install both
components follow the setup instructions located 
[here](https://github.com/openai/mujoco-py). This package should work 
with all versions of MuJoCo (with some changes likely to the version of 
`gym` provided).

### Importing AntGather

To properly import and run the AntGather environment, you will need to 
first clone and install the `rllab` library. You can do so running the 
following commands:

```
git clone https://github.com/rll/rllab.git
cd rllab
python setup.py develop
```

While all other environments run on all version of MuJoCo, this one will 
require MuJoCo-1.3.1. You may also need to install some missing packages
as well that are required by rllab. If you're installation is 
successful, the following command should not fail:

```
python experiments/run_fcnet.py
```
### Run I^2HRL


```
python run_comhrl.py "HalfCheetah-v2" --meta_period 10
```

here are an example of the parameter setting.

```
{
    "_init_setup_model": true,
    "actor_update_freq": 2,
    "env_name": "AntMaze",
    "meta_update_freq": 10,
    "nb_eval_episodes": 50,
    "nb_rollout_steps": 1,
    "nb_train_steps": 1,
    "policy_kwargs": {
        "actor_lr": 0.0003,
        "batch_size": 128,
        "buffer_size": 200000,
        "centralized_value_functions": false,
        "cg_weights": 0.0005,
        "connected_gradients": false,
        "critic_lr": 0.0003,
        "gamma": 0.99,
        "layer_norm": false,
        "meta_period": 10,
        "noise": 0.1,
        "off_policy_corrections": false,
        "relative_goals": true,
        "target_noise_clip": 0.5,
        "target_policy_noise": 0.2,
        "tau": 0.005,
        "use_fingerprints": false,
        "use_huber": true,
        "worker_reward_scale": 1
    },
}
```

