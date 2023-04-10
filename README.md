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
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt} => picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}
```

### variable_rot.py
It takes the input from the command that runs the Python Program. But the first argument that is passed should be the shift value. ROT13 has a shift value of 13 so we don't have to provide a shift value for rot13.py.<br />
For example:
```bash
python variable_rot.py shift string_1 string_2 ...
```
And will give the output in the same format as that of rot13.py