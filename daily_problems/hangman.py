# Create a function that, given a phrase and a number of letters guessed,
# returns a string with hyphens - for every letter of the phrase not guessed, and each letter guessed in place.
#
# Examples
# hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"
#
# hangman("tree", ["r", "t", "e"]) ➞ "tree"
#
# hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"
#
# hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"
# Notes
# The letters are always given in lowercase,
# but they should be returned in the same case as in the original phrase (see example #3).
# All characters other than letters should always be returned (see example #4).
def hangman(phrase, guessed):
    result = ""
    for char in phrase:
        if char.isalpha() and char.lower() not in guessed:
            result += "-"
        else:
            result += char
    return result
print(hangman("helicopter", ["o", "e", "s"]))
print(hangman("tree", ["r", "t", "e"]))
print(hangman("He's a very naughty boy!", ["e", "a", "y"]))

# def hangman(phrase, guessed):
#     result = []
#     for char in phrase:
#         if char.isalpha() and char.lower() not in guessed:
#             result.append("-")
#         else:
#             result.append(char)
#     return result
#
#
# phrase = "helicopter"
# guessed = ["o", "e", "s"]
# result = hangman(phrase, guessed)
# print(result)
# result_str = ''.join(result)
# print(result_str)
# phrase1 = "tree"
# guessed1 = ["r", "t", "e"]
# result2 = hangman(phrase1, guessed1)
# print(result2)
# resul2_str = ''.join(result2)
