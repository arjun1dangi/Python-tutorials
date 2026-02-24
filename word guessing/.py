import random
import string

n = random.choice(string.ascii_uppercase)
a = ""
guesses = 0
while a != n:
    guesses += 1
    a = input("Guess the alphabet: ").upper()
    if a.lower() > n.lower():
        print("Guess a lower alphabet")
    else:
        print("Guess a higher alphabet")

print(f"You have guessed the alphabet {n} correctly in {guesses} attempts")