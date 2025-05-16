import random

# Setup
choices = {'R': "Rock", 'P': "Paper", 'S': "Scissors"}
user_score = comp_score = 0

# Game count
rounds = int(input("\nHow many rounds do you want to play? "))

while user_score + comp_score < rounds:
    user_input = input("\nYour move (Rock/Paper/Scissors): ").strip().upper()[0]

    if user_input not in choices:
        print("Invalid input. Try again.")
        continue

    comp_input = random.choice(list(choices))
    print(f"Computer chose: {choices[comp_input]}")

    if (user_input, comp_input) in [('R', 'S'), ('P', 'R'), ('S', 'P')]:
        user_score += 1
        print("You win this round!")
    elif user_input == comp_input:
        print("It's a tie!")
    else:
        comp_score += 1
        print("Computer wins this round!")

    print(f"\nScore -> You: {user_score} | Computer: {comp_score}")

# Final result
print("\nFinal Score:")
print(f"You: {user_score} | Computer: {comp_score}")

if user_score > comp_score:
    print("\n Congratulations! You won!")
elif user_score < comp_score:
    print("\nYou lost. Better luck next time!")
else:
    print("\n It's a tie!")
