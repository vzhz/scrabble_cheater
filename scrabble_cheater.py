import sys

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
"x": 8, "z": 10}

valid_words = []

f = open('sowpods.txt', 'r').read().split()
for i in f:
    valid_words.append(i.lower())

rack = sys.argv[1].lower()
if len(rack) != 7 or rack.isalpha() is False: #the "only letters" test doesn't work #also blanks
    print("Please rerun command and seven-letter rack to play.")
    exit()

winning_words = []
for word in valid_words:
    rack_temp = list(rack)
    for letter in word:
        if letter in rack_temp:
            rack_temp.remove(letter)
            if len(rack) - len(rack_temp) == len(word):
                winning_words.append(word)

def add_points_word(word):
    points_word = 0
    for letter in word:
        if letter in scores: #scores letters are strings might need to split the words in valid words into their individual letters
            points_word += scores[letter]
    return points_word

just_points_winning_words = []
for word in winning_words:
    points_word = add_points_word(word)
    just_points_winning_words.append(points_word)

winning_words_and_points = dict(zip(winning_words, just_points_winning_words))

#sorting dict by value so the words that give you the most points are listed first
print("")
print("For the maximum points, spell this word: " + max(winning_words_and_points, key=winning_words_and_points.get))
print("")