#Scrabble was made using instructions found at https://openhatch.org/wiki/Scrabble_challenge

import sys
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

valid_words = []

f = open('sowpods.txt', 'r').read().split() #from http://stackoverflow.com/questions/13656519/python-how-to-get-rid-of-r-in-string
for i in f:
	valid_words.append(i.lower())

#print sys.argv gives ['scrabble.py', '<whatever I typed after command in terminal>']
rack = sys.argv[1].lower()
if len(rack) !=8 or rack.isalpha() is False: #the "only letters" test doesn't work
	print "Please rerun command and eight-letter rack to play."
	exit()

#print type(valid_words[0]), valid_words[0]
winning_words = []
for word in valid_words:
	rack_temp = rack
	for letter in word:
		if letter in rack_temp:
			k = rack_temp.index(letter)
			rack_temp = rack_temp[:k] + rack_temp[k+1:]
	if len(rack)-len(rack_temp)==len(word):
		winning_words.append(word)

#winning_words_and_points = dictfromkeys(winning_words)
#^(see above) http://stackoverflow.com/questions/20079681/initializing-a-dictionary-in-python-with-a-key-value-and-no-corresponding-values
just_points_winning_words = []
for word in winning_words:
	points_word = 0
	for letter in word:
		if letter in scores: #scores letters are strings might need to split the words in valid words into their individual letters
			points_word += scores[letter]
			just_points_winning_words.append(points_word)
	winning_words_and_points = dict(zip(winning_words, just_points_winning_words)) #http://stackoverflow.com/questions/8080890/initialize-dict-with-keys-values-from-two-list
	#print winning_words_and_points

#sorting dict by value so the words that give you the most points are listed first
print "For the maxium points, spell this word: " + max(winning_words_and_points, key=winning_words_and_points.get)
