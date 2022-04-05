# zipcodelib
This is a Python library to validate and format United Kingdom zipcodes.

- Pre-requisites: [Python3](https://www.python.org/downloads/)

### Installation
```
git clone https://github.com/hv-leo/zipcodelib
python setup.py bdist_wheel
pip install dist/zipcodelib-1.0-py3-none-any.whl
```

### Usage
```
from zipcodelib import validator, formatter
validator.str_format("EC1A1BB") => EC1A 1BB
validator.is_valid("EC1A 1BB")  => True
```

### Run the Tests
```
pip install -r requirements.txt
pytest
```

## Authors:
- Leonardo Coelho: <leonardo.coelho@ua.pt>