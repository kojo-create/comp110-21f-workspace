"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730402712"

from random import randint

random_number: int = randint(1, 4)
print("Your fortune cookie says...")

if random_number < 2:
    print("There is a great romance in you future, you are going to fall in love with a very powerful bender!")    
else:
    if random_number == 3:
        print("You are going to be involved in a great battle between the forces of good and evil which will determine the fate of the world!")
    else:
        if random_number == 4:
            print("You are going to be with the one you love if you trust your heart! :-)")
        else:
            print("Your future is going to be full of struggle and anguish, most of it will be self-inflicted! :-(")    
print("Now, go spread positive vibes!")