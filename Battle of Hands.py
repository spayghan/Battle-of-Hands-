import random
'''0 for stone
   1 for paper
   2 for scissors'''

choice = {"s": 0, "p": 1, "c": 2}
reverseChoice = {0: "stone", 1: "paper", 2: "scissor"}

player_score = 0
computer_score = random.choice([0, 1, 2])
rounds = 3

for i in range(rounds):
    mychoice = input("Enter your choice (s=stone, p=paper, c=scissor): ").lower()
    
    if mychoice not in choice:
        print("Invalid choice! Try again.")
        continue
    
    computer = random.choice([0, 1, 2])
    you = choice[mychoice]
    
    print(f"\nRound {i+1}")
    print(f"You chose: {reverseChoice[you]}")
    print(f"Computer chose: {reverseChoice[computer]}")

    if computer == you:
        print("Result: Draw")
    elif (computer == 0 and you == 1) or (computer == 1 and you == 2) or (computer == 2 and you == 0):
        print("Result: You win!")
        player_score += 1
    else:
        print("Result: You lose!")
        computer_score += 1

print(f"\nFinal score -> You: {player_score}, Computer: {computer_score}")

if player_score > computer_score:
    print("You win the game!")
elif player_score < computer_score:
    print("You lose the game!")
else:
    print("The game is a draw!")
