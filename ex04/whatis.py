import sys


if len(sys.argv) > 2:
    raise AssertionError("more than one argument is provided")

if len(sys.argv) == 1:
    sys.exit(0)

try:
    number = int(sys.argv[1])
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    raise AssertionError("argument is not an integer") from None
