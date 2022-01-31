# Beta Decay Chain Generator
This program was developed by Katelyn Watts, under supervision and guidance from Dr. Roger Caballero-Folch, at and for TRIUMF: Canada's Particle Acceleration Centre.

## The Gist

This is  a short program where users provide a nuclide that undergoes ß- decay and receive a csv file containing all the possible decay chains and the probability of each step. The program accounts for nonzero P1n and P2n values.

## Installation

tbd, likely making sure you've installed python and pandas


## Input

The program launches with a tkinter interface. The user is prompted to enter a nuclide that undergoes ß- decay as well as a path for the csv. The csv is written to a file called `Decay_Chain_[nuclide].csv` in the user-specified directory. If no directory is specified, the default is `~/Downloads/`. 

There will also be a checkbox called print. If selected, the decay chains will be printed to the console in the form of a Python list.

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
The csv file structure is very basic. The entered nuclide is listed in the first column of each row, followed by its probability of either emitting zero, one, or two neutrons. This is followed by the next nuclide in the chain and the same type of probability. The chain terminates once a stable nuclide is reached. Since the last nuclide in each chain is stable, it is not followed by a probability value. Since some chains will be shorter than others, some rows will have some blank elements. 

#### Special Values
There are some probability values that are to be treated as flags, and have special meanings. In both cases, the nuclide's P1n or P2n value is unknown, but the specified number of neutron emissions is known to occur. 
| Value       | Meaning     |
| :---------- | :---------- |
| -1.0/-1     | The nuclide's Qß1n or Qß2n value is extremely large and has not been measured. |
| 0.001       | The nuclide's Qß1n or Qß2n value is less than 1000 MeV and has not been accurately measured.  |


Sample Output (csv file):

```python
88As,-1.0,88Se,99.01,88Br,93.28,88Kr,100.0,88Rb,100.0,88Sr
88As,-1.0,87Se,99.4,87Br,97.47,87Kr,100.0,87Rb,,
88As,-1.0,86Se,-1.0,86Br,100.0,86Kr,,,,
88As,-1.0,88Se,0.99,87Br,97.47,87Kr,100.0,87Rb,,
88As,-1.0,87Se,0.60,86Br,100.0,86Kr,,,,
88As,-1.0,86Se,-1.0,85Br,100.0,85Kr,100.0,85Rb,,
88As,-1.0,88Se,99.01,88Br,6.72,87Kr,100.0,87Rb,,
88As,-1.0,87Se,99.4,87Br,2.53,86Kr,,,,
88As,-1.0,88Se,0.99,87Br,2.53,86Kr,,,,
88As,-1.0,88Se,99.01,88Br,6.72,87Kr,100.0,87Rb,,
88As,-1.0,87Se,99.4,87Br,2.53,86Kr,,,,
```
Sample Output (printed to console if print box checked):

```python
['88As', -1.0, '88Se', 99.01, '88Br', 93.28, '88Kr', 100, '88Rb', 100, '88Sr']
['88As', -1.0, '87Se', 99.4, '87Br', 97.47, '87Kr', 100, '87Rb']
['88As', -1.0, '86Se', -1.0, '86Br', 100, '86Kr']
['88As', -1.0, '88Se', 0.99, '87Br', 97.47, '87Kr', 100, '87Rb']
['88As', -1.0, '87Se', 0.6, '86Br', 100, '86Kr']
['88As', -1.0, '86Se', -1.0, '85Br', 100, '85Kr', 100, '85Rb']
['88As', -1.0, '88Se', 99.01, '88Br', 6.72, '87Kr', 100, '87Rb']
['88As', -1.0, '87Se', 99.4, '87Br', 2.53, '86Kr']
['88As', -1.0, '88Se', 0.99, '87Br', 2.53, '86Kr']
['88As', -1.0, '88Se', 99.01, '88Br', 6.72, '87Kr', 100, '87Rb']
['88As', -1.0, '87Se', 99.4, '87Br', 2.53, '86Kr']
```
