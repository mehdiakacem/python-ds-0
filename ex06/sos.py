import sys


def main():
    """Encode a command-line message in Morse code."""
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    text = sys.argv[1].upper()
    mapping = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/",
    }
    codes = []

    for char in text:
        if char in mapping:
            codes.append(mapping[char])
        else:
            raise AssertionError("the arguments are bad")
    print(" ".join(codes))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")
