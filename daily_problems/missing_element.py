# ou are given two lists. The elements in lst1 threw a party and started to mix around.
# However, one of the elements got lost! Your task is to return the element which was lost.
#
# Examples
# missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]) ➞ 2
#
# missing([True, True, False, False, True], [False, True, False, True]) ➞ True
#
# missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]) ➞ "ugly"
#
# missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]) ➞ (5,)
# Notes
# Assume that the first list always contains 1 or more elements.
# Elements are always lost.
# An element can also have duplicates.

from collections import Counter


def convert_to_tuple(item):
    if isinstance(item, list):
        return tuple(convert_to_tuple(element) for element in item)
    else:
        return item


def missing(lst1, lst2):
    count1 = Counter(convert_to_tuple(lst1))
    count2 = Counter(convert_to_tuple(lst2))

    lst_count = count1 - count2

    for element, count in lst_count.items():
        if count > 0:
            return element
    return None


print(missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]))
print(missing([True, True, False, False, True], [False, True, False, True]))
print(missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]))
print(missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]))


