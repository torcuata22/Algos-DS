import random
#dice game
high_score = 0



def dice_game():
    global high_score
    roll_dice = "yes"
    print("Your current High Score:", high_score)
    print("1) Roll the dice")
    print("2) Leave the game")
    x = input("Enter your choice")
    print("\n")


    while roll_dice =="yes" or roll_dice  == "y":
        if x == "1":
            roll_dice1 = random.randint(1, 6)
            roll_dice2 = random.randint(1, 6)
            total_roll = roll_dice1 + roll_dice2
            print("You rolled a ", roll_dice1)
            print("You rolled a", roll_dice2)
            print("You have rolled a total of:", total_roll)

            if high_score < total_roll:
                high_score = total_roll + high_score
                print("Congratulations! You have a new high score:", total_roll)

            if total_roll < high_score:
                high_score = total_roll + high_score
                print("Your high score is", high_score)
                
            print("select yes or no")
            roll_dice = input("Roll the dice again?")
        else:
            print("Goodbye!")
    




dice_game()
