games_played = 0
computer_wins = 0

print("=== Welcome to the Number Guessing Game! ===")

while True:
    try:
        x = int(input("\nEnter a secret number between 1 and 1000 for the computer to guess: "))
        if not (1 <= x <= 1000):
            print("Please pick a number between 1 and 1000.")
            continue
    except ValueError:
        print("Please enter a valid integer.")
        continue

    low = 1
    high = 1000
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1
        print(f"Computer guesses: {guess}")

        if guess == x:
            games_played += 1
            computer_wins += 1
            print(f"\n🎉 Computer WINS in {attempts} attempts!")
            break
        elif guess < x:
            print("Computer guessed too low")
            low = guess + 1
        else:
            print("Computer guessed too high")
            high = guess - 1

    # Ask user if they want to continue
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again not in ['y', 'yes']:
        print(f"\nThanks for playing! Total games played: {games_played}, Computer wins: {computer_wins}")
        break