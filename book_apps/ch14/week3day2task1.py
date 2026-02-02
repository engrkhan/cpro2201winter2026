
import random as rd

class Die:
    n:int = 1

    def roll(self):
        self.n = rd.randint(1,7)

die = Die()

die.roll()

# print(f"Pssst, the correct answer is {n}")
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 6.")
print("Can you guess what it is?")
guess = int(input("Make a guess: "))
print("You guessed ", guess)
while guess != die.n:
  if guess > die.n:
    print("Too high")
  else:
    print("Too low")
  guess = int(input("Try again: "))

print("You have got it!")

print(f"The correct answer is: {guess}")