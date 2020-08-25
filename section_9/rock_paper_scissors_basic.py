# Ask the players their name
p1_name = input('Player 1, what is your name? : ').capitalize()
p2_name = input('Player 2, what is your name? : ').capitalize()

print("Choices: \n 1).Rock \n 2).Paper \n 3).Scissors")
p1 = input(f'{p1_name} Chooses : ').capitalize()

# Print some stuff to keep player 1 choice hidden
for x in range(30) :
    print("** No Cheating **")

p2 = input(f'{p2_name} Chooses : ').capitalize()

# 1 (rock) over 3 (scissors)
if p1 == "Rock" and p2 == "Scissors":
    print(f"{p1_name} wins!")
elif p1 == "Rock" and p2 == "Paper":
    print(f"{p2_name} wins!")

# 2 (paper) over 1(rock)
elif p1 == "Paper" and p2 == "Rock":
    print(f"{p1_name} wins!")
elif p1 == "Paper" and p2 == "Scissors":
    print(f"{p2_name} wins!")

# 3 (scissors) over 2 (paper)
elif p1 == "Scissors" and p2 == "Paper":
    print(f"{p1_name} wins!") 
elif p1 == "Scissors" and p2 == "Rock":
    print(f"{p2_name} wins!")

# if they are the same it's a draw.
elif p1 == p2:
    print("It's a draw")

# Catch all for errors
else:
    print("Something went wrong")