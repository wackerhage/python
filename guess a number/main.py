from art import logo
import random

game = True
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
attempts: 0
right_answer = 0

while game is True:
  print(logo)

  print("Welcome to the Super Guessing!")
  print("Are you ready to win?!")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  right_answer = random.choice(numeros)
  if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts.")
  if difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} attempts.")
  while attempts != 0:
    guess = int(input("Make a guess: "))
    if guess == right_answer:
      print(f"You got it! The answer is {right_answer}.")
      game = False
      attempts = 0
    if guess != right_answer:
      if guess < right_answer:
        attempts -= 1
        print("Too low! Guess Again.")
        print(f"You have {attempts} attempts left.")
      if guess > right_answer:
        attempts -= 1
        print("To high! Guess Again.")
        print(f"You have {attempts} attempts left.")
    if attempts == 0:
      print("Game over!")

  reset = input("Do you want to play again? Type 'yes' or 'no': ")
  if reset == "yes":
    game = True
  if reset == "no":
    game = False
    print("Goodbye!")
  
  
