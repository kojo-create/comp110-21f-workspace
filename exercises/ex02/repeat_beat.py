"""Repeating a beat in a loop."""

__author__ = "730402712"


counter: int = 0
beat_type: str = input("What beat do you want to repeat? ")
play_limit: int = int(input("How many times do you want to repeat it? "))
beat: str = ""
while counter < play_limit:
    beat = beat + " " + beat_type
    counter = counter + 1
print(beat) 

if play_limit <= 0:
    print("No beat...")