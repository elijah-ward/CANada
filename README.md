# CANada
Controller Area Network Automatic Defense Architecture (CANada)

CANada is a prototype architecture for improving the security of a Connected Vehicle (CV) using Hardware Security Modules (HSM) to monitor the traffic on a CAN bus. Most code in this project is related to simulating a CAN bus and the behaviour of various Engine Control Units (ECU) and HSMs.

For the most consistent experience we recommend running the simulations in either **Linux** or **MacOS**.

## Getting Started

## Useful Tools

- `conda` - https://conda.io/miniconda.html (useful in managing multiple python environments, be sure to install Python 3.7 version)

### Conda

In this repository there is an `environment.yml` file that contains information about the dependencies required by this project. It also specifies `tso` as the name of the environment.

#### Creating a New Environment in Conda From an `environment.yml` File

```
conda env create -f environment.yml
```

#### Switching Environments Created Using Conda

**MacOS/Linux**
```
source activate can
```
**Windows**
```
activate can
```

## Running Trials to Gather Metrics

In order to run several iterations of the system to gather metrics about the behaviour, run the following command where `N_TRIALS` is the integer number of trials to run and `TRIAL_DURATION` is the duration of the trial in seconds:

```
python run_trials.py [N_TRIALS] [TRIAL_DURATION]
```


## Running the Simulation

The simulations will run until the process is killed by the user. To do so press `ctrl+c`.

In order to run each of the simulations, execute the following:

#### Frequency Moderation Security Simulation
```
python freq_simulation.py
```

#### Authentication Security Simulation
```
python auth_simulation.py
```

#### Intrusion Detection Simulation
```
python intrusion_simulation.py
```

## Maintainers

- [Elijah Ward](https://github.com/elijah-ward)
- [Zain Hemani](https://github.com/zhemani)
- [Veronica Witzig](https://github.com/VeronicaWitzig)
- [Chuanheng He](https://github.com/henryhehe)
- [Samir Kazi](https://github.com/SamirK15)
