"""Counting letters in a string."""

__author__ = "730402712"


character: str = input("What letter do you want to search for?: ")
word_choice: str = input("Enter a word: ")
counter: int = 0
checker: int = 0

while checker < len(word_choice):
    if character == word_choice[checker]:
        counter = counter + 1
    checker = checker + 1           
print("Count: " + str(counter))