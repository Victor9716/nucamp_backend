import random


current_score = 0


def dice_game():

    high_score = 0

    while True:
        print("1. Roll Dice")
        print("2. Leave Game")
        
        choice = input("Enter your choice: ")

        if  choice == '1':
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
            print('You rolled a',dice1,'and a',dice2)
            print('The total is ',total)
        # update the score
            if total > high_score:
                high_score = total
                print("New  High Score!: ", high_score)
        elif choice == "2":
            print("\nThanks for playing.")
            break
        else:
            print("Invalid Choice\nPlease enter again")
    

dice_game()
