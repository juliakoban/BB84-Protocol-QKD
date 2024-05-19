# BB84 Protocol

## Description 
This project is an implementation of BB84 Quantum Key Distribution protocol build with Python.

## How To Use
This project's display relies on the [termcolor library](https://pypi.org/project/termcolor/). Before running, ensure that termcolor module is installed on your system.

Define parameters in qkd_bb84.py file:
1. bit_string_length - length of the transmitted information
2. printing_length - number of bits displayed on the screen
3. error - channel disturbance error (in %)
4. change eve = None in order to stop eavesdropping

Example parameters:
```
bit_string_length = 1000
printing_length = 20
error = 0
```
Run:
```
python3 qkd_bb84.py
```
