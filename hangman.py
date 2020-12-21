from random_word import RandomWords
import re
r = RandomWords()
rand_word = r.get_random_word()
print(rand_word)
underscored_word = "_"
count_underscores = 1
space_occurrences = [m.start() for m in re.finditer(" ", rand_word)]
while count_underscores < len(rand_word):
    underscored_word += "_"
    count_underscores += 1


# Gotta add spaces back in

nextLetter = input("Guess a letter: ")
if len(nextLetter) > 1:
    print("Can't be more than 1 letter!")
elif nextLetter in rand_word:
    occurrences = [m.start() for m in re.finditer(nextLetter, rand_word)]
    print("There are " + str(len(occurrences)) + " " + nextLetter + "'s in the word")
    print(occurrences)
    underscored_word = underscored_word[:occurrences[0]] + nextLetter + underscored_word[occurrences[0]+1:]
    spaced_underscored_word = underscored_word
    count = 0
    while count < len(underscored_word):
        spaced_underscored_list = list(spaced_underscored_word)
        spaced_underscored_list.insert(count+count, " ")
        spaced_underscored_word = ''.join(spaced_underscored_list)
        count += 1

    print(spaced_underscored_word)
else:
    print("The word has no " + nextLetter + "'s.")

