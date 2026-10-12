import string
import sys


def main():
    """Count characters by category in the provided text."""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("too many arguments")
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    if len(sys.argv) == 1:
        print("What is the text to count?")
        text = sys.stdin.readline()
    else:
        text = sys.argv[1]

    print(f"The text contains {len(text)} characters:")

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1

    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    main()
