#!/usr/bin/env python
#SUFI N RAFIK
import random

def main():
    """Start a music guessing game."""
    print("Guess the music!")

    songs = [
      "Nazam Lebaran",
      "Air Mata Syawa",
      "Nikmat Hari Raya",
      "Bila Hari Raya Menjelma",
      "Anugerah Aidilfitri"
    ]
 
    x = random.choice(song)
    guess = None 

    while x !=guess:
      
        guess = str(input("What song am i thinking of? "))

        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break   
        else:
            print("You guessed {}.Unfortunately you got the answer. Please try again!".format(guess)) 
                  
main()