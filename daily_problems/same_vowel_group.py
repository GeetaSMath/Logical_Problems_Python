# Write a function that selects all words that have all the same vowels
# (in any order and/or number) as the first word, including the first word.
#
# Examples
# same_vowel_group(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]
#
# same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) ➞ ["many"]
#
# same_vowel_group(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]
# Notes
# Words will contain only lowercase letters, and may contain whitespaces.
# Frequency does not matter (e.g. if the first word is "loopy", then you can include words with any
# number of o's, so long as they only contain o's, and not any other vowels).

def same_vowel_group(words):
    first_word_vowels = set(ch for ch in words[0] if ch in 'aeiou')
    result = [words[0]]

    for word in words[1:]:
        word_vowels=set(ch for ch in word if ch in 'aeiou')
        if word_vowels==first_word_vowels:
            result.append(word)

    # for word in words[1:]:
    #     if all(vowel in vowels for vowel in word) and all(vowel in word for vowel in vowels):
    #         result.append(word)
    return result


print(same_vowel_group(["toe", "ocelot", "maniac"]))
print(same_vowel_group(["hoops", "chuff", "bot", "bottom"]))
print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))