x = int(input("Enter number between(1-1000): "))

low = 1
high = 1000
attempts = 0
while True:
    guess = (low + high) // 2
    print(f"Computer guesses: {guess}")
    attempts += 1
    if guess == x:
        print(f"Computer WINS in {attempts} attempts!")
        break
    elif guess < x:
        print("Computer guessed too low")
        low = guess + 1
    else:
        print("Computer guessed too high")
        high = guess - 1