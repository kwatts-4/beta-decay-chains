# Beta Decay Chain Generator
This program was developed by Katelyn Watts, under supervision and guidance from Dr. Roger Caballero-Folch, at and for TRIUMF: Canada's Particle Acceleration Centre.

## The Gist

This is a short program where users provide a nuclide that undergoes ß- decay and can emit neutrons in that process. The user receives a csv file containing all the possible decay chains, the half-life of each nuclide, and the probability of each step.

## Installation

Before installing, make sure you have Python 3.6 or later installed. For information on how to install python, go to https://www.python.org/downloads/.

There are two options for installation of this program. 

* Cloning this Repository
  * From the console, navigate to the directory where you want the program
  * Enter `git clone https://github.com/kwatts-4/beta-decay-chains`
* Downloading the Program Directly
  * Go to https://github.com/kwatts-4/beta-decay-chains
  * Click code (the green button)
  * Click Download ZIP 
  * Unzip the file and move the directory into a directory of your choice


## Input

From the console, navigate to the directory called `beta-decay-chains`. If you downloaded the zip file rather than cloning the repository, the directory will be called `beta-decay-chains-main`. Once there, enter the command `python src/chain_generator/interface.py`. This will launch the program.

The program launches with a tkinter interface. The user is prompted to enter a nuclide that undergoes ß- decay as well as a path for the csv. The csv is written to a file called `Decay_Chain_[nuclide].csv` in the user-specified directory. If no directory is specified, the default is the current directory. 

There is also a checkbox which when selected will print the decay chains to the console as of Python lists.

Sample Inputs:
```python
88As
./
```
```python
98Rb
~/Downloads/User-Specified/Path/
```

## Output
The csv file structure is very basic. The entered nuclide is listed in the first column of each row, followed by its half-life in seconds, then its probability of either emitting zero, one, or two neutrons. This is followed by the next nuclide in the chain, its half-life, and its probability of producing the third nuclide in the chain. The chain terminates once a stable nuclide is reached. Since the last nuclide in each chain is stable, its half-life ('STABLE' or a half-life above 1e+18) is not followed by a probability value. Since some chains will be shorter than others, some rows will have a few blank elements. 

#### Special Values
There are some probability values that are to be treated as flags, and have special meanings. In both cases, the nuclide's P1n or P2n value is unknown, but the specified number of neutron emissions is known to occur. 
| Value       | Meaning     |
| :---------- | :---------- |
| -1.0/-1     | The nuclide's Qß1n or Qß2n value is extremely large and has not been measured. |
| 0.001       | The nuclide's Qß1n or Qß2n value is less than 1000 MeV and has not been accurately measured.  |


Sample Output (csv file):

```python
888As,0.20,-1.000,88Se,1.51,99.010,88Br,16.29,93.280,88Kr,10170,100.000,88Rb,1066.38,100.000,88Sr,STABLE
88As,0.20,-1.000,87Se,5.65,99.400,87Br,55.64,97.470,87Kr,4578,100.000,87Rb,1.56841E+18,,,
88As,0.20,-1.000,86Se,14.1,99.999,86Br,55.1,100.000,86Kr,STABLE,,,,,,
88As,0.20,-1.000,88Se,1.51,0.990,87Br,55.64,97.470,87Kr,4578,100.000,87Rb,1.56841E+18,,,
88As,0.20,-1.000,87Se,5.65,0.600,86Br,55.1,100.000,86Kr,STABLE,,,,,,
88As,0.20,-1.000,86Se,14.1,0.001,85Br,174,100.000,85Kr,338897066.4,100.000,85Rb,STABLE,,,
88As,0.20,-1.000,88Se,1.51,99.010,88Br,16.29,6.720,87Kr,4578,100.000,87Rb,1.56841E+18,,,
88As,0.20,-1.000,87Se,5.65,99.400,87Br,55.64,2.530,86Kr,STABLE,,,,,,
88As,0.20,-1.000,88Se,1.51,0.990,87Br,55.64,2.530,86Kr,STABLE,,,,,,
```
Sample Output (printed to console if print box checked):

```python
['88As', '0.20', -1.0, '88Se', '1.51', 99.01, '88Br', '16.29', 93.28, '88Kr', '10170', 100, '88Rb', '1066.38', 100, '88Sr', 'STABLE']
['88As', '0.20', -1.0, '87Se', '5.65', 99.4, '87Br', '55.64', 97.47, '87Kr', '4578', 100, '87Rb', '1.56841E+18']
['88As', '0.20', -1.0, '86Se', '14.1', 99.999, '86Br', '55.1', 100, '86Kr', 'STABLE']
['88As', '0.20', -1.0, '88Se', '1.51', 0.99, '87Br', '55.64', 97.47, '87Kr', '4578', 100, '87Rb', '1.56841E+18']
['88As', '0.20', -1.0, '87Se', '5.65', 0.6, '86Br', '55.1', 100, '86Kr', 'STABLE']
['88As', '0.20', -1.0, '86Se', '14.1', 0.001, '85Br', '174', 100, '85Kr', '338897066.4', 100, '85Rb', 'STABLE']
['88As', '0.20', -1.0, '88Se', '1.51', 99.01, '88Br', '16.29', 6.72, '87Kr', '4578', 100, '87Rb', '1.56841E+18']
['88As', '0.20', -1.0, '87Se', '5.65', 99.4, '87Br', '55.64', 2.53, '86Kr', 'STABLE']
['88As', '0.20', -1.0, '88Se', '1.51', 0.99, '87Br', '55.64', 2.53, '86Kr', 'STABLE']
```
