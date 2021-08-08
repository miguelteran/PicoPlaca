# PicoPlaca
A python tool to determine if a user can drive on a specific date and time given the "Pico y Placa" system

## Using the tool
To get a prediction, run the Python script [run_prediction.py](./run_prediction.py) from a terminal

```
python run_prediction.py ABC-123 2021-12-31 13:45:00
```
The script takes three inputs:
- A license plate composed by three upper case letters, a dash, and three digits
- A date with format YYYY-MM-DD
- A time with format hh:mm:ss

## Running tests
Unit tests are located in the [test_pico_placa.py](tests/test_pico_placa.py) file. To run them, use the following command:
```
python -m unittest -v
```
or run the script:
```
python tests/test_pico_placa.py -v
```

## Limitations
The following "Pico y Placa" schedule is currently hard-coded:
- Monday - 0,1
- Tuesday - 2,3
- Wednesday - 4,5
- Thursday - 6,7
- Friday - 8,9
- Weekend - no restrictions
- Times: 7:00 - 9:30, 16:00 - 19:30

A future improvement will be to make it configurable.
