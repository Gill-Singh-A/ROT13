# ROT13
ROT13 is an encryption algorithm that uses simple letter substitution cipher and shifts the alphabets by a value of 13

## Requirements
Language Used = Python3
Modules/Packages used:
* sys
* colorama

### rot13.py
It takes the input strings from the command that runs the Python Program. <br />
For example:
```bash
python rot13.py string_1 string_2 ...
```
And will give the output in the format : input_string => rot13_string<br />
For example:
```bash
SSBMb3ZlIEhlciBfLl9fIC4uX19fIC5fX19fIC8gXy5fLiAuLi4gLg== => FFOZo3MyVRuypvOsYy9sVP4hK19sVP5sK19sVP8tKl5sYvNhYv4tYt==
```

### variable_rot.py
It takes the input from the command that runs the Python Program. But the first argument that is passed should be the shift value. ROT13 has a shift value of 13 so we don't have to provide a shift value for rot13.py.<br />
For example:
```bash
python variable_rot.py shift string_1 string_2 ...
```
And will give the output in the same format as that of rot13.py

## all_rot.py
It takes the input strings from the command that runs the Python Program. <br />
For example:
```bash
python rot13.py string_1 string_2 ...
```
And will give the output in the same format as that of rot13.py but for all Rotations.
