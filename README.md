# Beta Decay Chain Generator
This program was developed by Katelyn Watts, under supervision and guidance from Dr. Roger Caballero-Folch, at and for TRIUMF: Canada's Particle Acceleration Centre.

## The Gist

This is  a short program where users provide a nuclide that undergoes ß- decay and receive a csv file containing all the possible decay chains and the probability of each step. The program accounts for nonzero P1n and P2n values.

## Installation

tbd, likely making sure you've installed python and pandas


## Input

The program launches with a tkinter interface. The user is prompted to enter a nuclide that undergoes ß- decay as well as a path for the csv. The csv is written to a file called `Decay_Chain_[nuclide].csv` in the user-specified directory. If no directory is specified, the default is `~/Downloads/`.

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
The csv file structure is very basic. The entered nuclide is listed in the first column of each row, followed by its probability of either emitting zero, one, or two neutrons. This is followed by the next nuclide in the chain and the same type of probability. The chain terminates once a stable nuclide is reached; the last nuclide in each chain is stable.

#### Negative Numbers
There are some probability values that are listed as negative. They are to be interpreted as follows.
| Value       | Meaning     |
| :---------- | :---------- |
| -1.0/-1     | Probability value is unknown, but the specified number of neutron emissions is known to occur.       |
| -2.0/-2     | The nuclide is not in the database of selected nuclides undergoing ß- decay, therefore its probability values are unknown.  |

Note that stable nuclides necessarily do not undergo ß- decay, so their probability values will always be listed as -2.0/-2. 

Sample Output:

```python
88As,-1.0,88Se,99.01,88Br,93.28,88Kr,-2,88Rb,-2.0,88Sr,-2.0
88As,-1.0,87Se,99.4,87Br,97.47,87Kr,-2,87Rb,-2.0,,
88As,-1.0,86Se,-1.0,86Br,-2.0,86Kr,-2,,,,
88As,-1.0,88Se,0.99,87Br,97.47,87Kr,-2,87Rb,-2.0,,
88As,-1.0,87Se,0.6,86Br,-2.0,86Kr,-2,,,,
88As,-1.0,86Se,-1.0,85Br,-2.0,85Kr,-2,85Rb,-2.0,,
88As,-1.0,88Se,99.01,88Br,6.72,87Kr,-2,87Rb,-2.0,,
88As,-1.0,87Se,99.4,87Br,2.53,86Kr,-2,,,,
88As,-1.0,88Se,0.99,87Br,2.53,86Kr,-2,,,,
88As,-1.0,88Se,99.01,88Br,6.72,87Kr,-2,87Rb,-2.0,,
88As,-1.0,87Se,99.4,87Br,2.53,86Kr,-2,,,,
```

