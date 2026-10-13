import sys


def main():
    """Print words whose lengths exceed the given limit."""
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    try:
        limit = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    words = [word for word in sys.argv[1].split(" ") if word]
    result = list(filter(lambda word: len(word) > limit, words))
    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")
