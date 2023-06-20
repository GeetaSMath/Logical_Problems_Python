# Given a sentence as txt, return True if any two adjacent words have this property:
# One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
#
# Examples
# vowel_links("a very large appliance") ➞ True
#
# vowel_links("go to edabit") ➞ True
#
# vowel_links("an open fire") ➞ False
#
# vowel_links("a sudden applause") ➞ False
# Notes
# You can expect sentences in only lowercase, with no punctuation.
#iterator and generatores
class VowelLinkChecker:
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']

    def has_vowel_link(self, txt):
        words = txt.split()

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if word1[-1] in self.vowels and word2[0] in self.vowels:
                return True

        return False
checker = VowelLinkChecker()

print(checker.has_vowel_link("a very large appliance"))
print(checker.has_vowel_link("go to edabit"))
print(checker.has_vowel_link("an open fire"))
print(checker.has_vowel_link("a sudden applause"))
