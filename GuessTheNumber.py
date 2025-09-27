import random

secret_number = random.randint(1, 100)
guess_count = 0

print("Guess a number (1-100).")

while True:
    try:
        user_input = input("Guess: ")
        guess = int(user_input)
        guess_count += 1
    except ValueError:
        continue
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print(f"Correct! ({guess_count} guesses)")
        break