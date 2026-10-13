def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item


def main():
    """Demonstrate filtering even numbers."""
    print(list(ft_filter(lambda value: value % 2 == 0, range(10))))


if __name__ == "__main__":
    main()
