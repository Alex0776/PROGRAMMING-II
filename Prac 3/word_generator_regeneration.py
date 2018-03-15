import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    word_format = "cvccvcv"
    word = ""
    for kind in word_format:
            if kind == "c":
                word += random.choice(CONSONANTS)
            elif kind == "v":
                word += random.choice(VOWELS)
            else:
                is_valid_format(word)
print(word)

#WAIT, THERE HAS BEEN NO USER INPUT WHAT IS THIS QUESTION EVEN ASKING

main()