# CANada
Controller Area Network Automatic Defense Architecture (CANada)

CANada is a prototype architecture for improving the security of a Connected Vehicle (CV) using Hardware Security Modules (HSM) to monitor the traffic on a CAN bus. Most code in this project is related to simulating a CAN bus and the behaviour of various Engine Control Units (ECU) and HSMs.

## Getting Started

## Useful Tools

- `conda` - https://conda.io/miniconda.html (useful in managing multiple python environments)

### Conda

In this repository there is an `environment.yml` file that contains information about the dependencies required by this project. It also specifies `tso` as the name of the environment.

#### Creating a New Environment in Conda From an `environment.yml` File

```
conda create -f environment.yml
```

#### Switching Environments Created Using Conda

**MacOS/Linux**
```
source activate canada
```
**Windows**
```
activate canada
```

## Running the Simulation

In order to run the simulation, execute the following:
```
python simulation.py
```

## TODO / Roadmap

- Add additional vehicles/simulations for compromised scenarios
- Add dispatching of certain messages to bus by ECU (inter-bus)
- Implement various HSM defense strategy algos
- specified by "mode" HSM is started in
- Create adversarial nodes on bus
- DDOS node
- Replay attack node


- [DONE] provide some kind of configuration for normal driving behaviour 
- [DONE] finish assigning id's to each component and a proper mask

## Maintainers

- [Elijah Ward](https://github.com/elijah-ward)
- [Zain Hemani](https://github.com/zhemani)
- [Veronica Witzig](https://github.com/VeronicaWitzig)
- [Chuanheng He](https://github.com/henryhehe)
- [Samir Kazi](https://github.com/SamirK15)
