# Have a Python dictionary that has a key/value pair that represents a word and it is definition
# Collect input from the user, input is a word
# Check if the word is in the dictionary
# Print th definition
# TODO ! $ pip3 install PyDictionary

from PyDictionary import PyDictionary

# Method 1
dictionary = PyDictionary("eyes", "indentation", "head")
# print(dictionary.printMeanings())
print(dictionary.getMeanings())

# Method 2
""" dictionary = PyDictionary()

while True:
  word = input("Enter your word: ")
  if word == "":
    break
  print(dictionary.meaning(word))
"""
