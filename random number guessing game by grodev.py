import random

def generate_secret_number(difficulty):
  """Generates a secret number based on the chosen difficulty."""
  if difficulty == "easy":
    return random.randint(1, 10)
  elif difficulty == "medium":
    return random.randint(1, 100)
  else:
    return random.randint(1, 1000)

def play_game():
  """Starts the number gazing game."""
  difficulty = input("Choose difficulty (easy, medium, hard): ")
  secret_number = generate_secret_number(difficulty)
  guesses = 0
  max_guesses = 10

  while guesses < max_guesses:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess == secret_number:
      print("Congratulations! You guessed the number in", guesses, "guesses.")
      break
    elif guess < secret_number:
      print("Your guess is too low. Try again!")
    else:
      print("Your guess is too high. Try again!")

  if guesses == max_guesses:
    print("Sorry, you ran out of guesses. The secret number was", secret_number)

if __name__ == "__main__":
  play_game()
