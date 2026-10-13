# ft_package

A small Python package that counts matching values in a list.

## Installation

From the `ex09` directory, install either distribution file:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```
