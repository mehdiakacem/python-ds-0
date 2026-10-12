import math
from typing import Any


def NULL_not_found(object: Any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
        return 0
    elif type(object) is float and math.isnan(object):
        print("Cheese:", object, type(object))
        return 0
    elif type(object) is int and object == 0:
        print("Zero:", object, type(object))
        return 0
    elif type(object) is str and object == "":
        print("Empty:", object, type(object))
        return 0
    elif type(object) is bool and object is False:
        print("Fake:", object, type(object))
        return 0
    else:
        print("Type not Found")
        return 1
