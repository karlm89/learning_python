game_type = input('Are you playing against a human, or a computer? ').captitalize()

if game_type == 'Human':
    # Ask the players their name
    p1_name = input('Player 1, what is your name? : ').capitalize()
    p2_name = input('Player 2, what is your name? : ').capitalize()

    print("Choices: \n 1).Rock \n 2).Paper \n 3).Scissors")
    p1 = input(f'{p1_name} Chooses : ').capitalize()

    # Print some stuff to keep player 1 choice hidden
    for x in range(40) :
        print("** No Cheating **")

    p2 = input(f'{p2_name} Chooses : ').capitalize()

    # if they are the same it's a draw.
    if p1 == p2:
        print("It's a draw")
    # 1 (rock) over 3 (scissors)
    elif p1 == "Rock":
        if p2 == "Scissors":
            print(f"{p1_name} wins!")
        elif p2 == "Paper":
            print(f"{p2_name} wins!")

    # 2 (paper) over 1(rock)
    elif p1 == "Paper":
        if p2 == "Rock":
            print(f"{p1_name} wins!")
        elif p2 == "Scissors":
            print(f"{p2_name} wins!")

    # 3 (scissors) over 2 (paper)
    elif p1 == "Scissors": 
        if p2 == "Paper":
            print(f"{p1_name} wins!") 
        elif p2 == "Rock":
            print(f"{p2_name} wins!")

    # Catch all for errors
    else:
        print("Something went wrong")

else: 
    import random
    # Ask the players their name
    p1_name = input('Player 1, what is your name? : ').capitalize()
    p2_name = "Computer"
    print("Choices: \n 1).Rock \n 2).Paper \n 3).Scissors")
    p1 = input(f'{p1_name} Chooses : ').capitalize()

    rand_num = random.randint(0,2)
    
    if rand_num == 0:
        p2 = "Rock"
    elif rand_num == 1:
        p2 = "Paper"
    elif rand_num == 2:
        p2 = "Scissors"

    print(f"{p2_name} chooses : {p2}")

    # if they are the same it's a draw.
    if p1 == p2:
        print("It's a draw")
    # 1 (rock) over 3 (scissors)
    elif p1 == "Rock":
        if p2 == "Scissors":
            print(f"{p1_name} wins!")
        elif p2 == "Paper":
            print(f"{p2_name} wins!")

    # 2 (paper) over 1(rock)
    elif p1 == "Paper":
        if p2 == "Rock":
            print(f"{p1_name} wins!")
        elif p2 == "Scissors":
            print(f"{p2_name} wins!")

    # 3 (scissors) over 2 (paper)
    elif p1 == "Scissors": 
        if p2 == "Paper":
            print(f"{p1_name} wins!") 
        elif p2 == "Rock":
            print(f"{p2_name} wins!")

    # Catch all for errors
    else:
        print("Something went wrong")