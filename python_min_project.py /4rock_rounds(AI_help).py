import random as rnd

def get_computer_choice():
    comp = rnd.choice(["rock", 'paper', 'scissor'])
    return comp

def get_player_choice():
    player = input('Rock OR Paper OR Scissor: ').lower()
    return player

def check_winner():
    p = get_player_choice()
    c = get_computer_choice()
    print(f"Computer chose: {c}")
    if c == p:
        return "Draw"
    elif c == "rock":
        if p == "paper":
            return "player"
        else:
            return "computer"
    elif c == "paper":
        if p == "scissor":
            return "player"
        else:
            return "computer"
    elif c == "scissor":
        if p == "rock":
            return "player"
        else:
            return "computer"

def play_match():
    # Ask how many rounds the player wants
    rounds = int(input("How many rounds do you want to play? "))
    
    player_score = 0
    computer_score = 0
    
    for i in range(rounds):
        print(f"\n--- Round {i + 1} ---")
        winner = check_winner()
        print(f"Winner of this round: {winner}")
        
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
            
    # Announce the final result
    print("\n===== FINAL RESULTS =====")
    print(f"Your Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    
    if player_score > computer_score:
        print("Congratulations! You won the overall match! 🎉")
    elif computer_score > player_score:
        print("Computer won the overall match! Better luck next time! 🤖")
    else:
        print("It's an overall tie! 🤝")

# Run the game match
play_match()