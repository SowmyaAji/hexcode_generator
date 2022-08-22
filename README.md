# hexcode_generator
Generate hexcodes for MFA

## Overview:

A hexcode generator in Python written with the following constraints:

- Every time the program is run, it should emit one 8-digit hexadecimal code;
- It should emit every possible code before repeating;
- It should not print "odd-looking" codes such as 0xAAAAAAAA or 0x01234567 or any commonly used words, phrases, or hexspeak such as 0xDEADBEEF;
- Codes should be emitted in apparently random order. 

## Requires:

- Python ^3.8
- Requests library ( ```pip install requests```)
- Beautiful Soup library (```pip install beautifulsoup4```)


## To use:

- clone repo and cd into it
- create venv or pipenv or pyenv or conda virtual env
- pip install the two libraries mentioned above
- run ```python generate_hex.py```
- to test, run ```python tests.py```

