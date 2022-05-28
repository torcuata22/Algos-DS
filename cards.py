import random
diamonds = ["1D", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]  # this is the deck
hand = []  # this is the list for the cards dealt to player

while diamonds: #while there are cards in the diamonds list, the loop will run
    x = input("Press enter to pick a card, or Q and then Enter to exit the game")
    print(str("Press enter to pick a card, or Q and then Enter to exit the game"))

    if x == "Q" or x == "q":
        print("You have chosen to leave the game. Good-bye!")
        break
    else:
        random.shuffle(diamonds)  # shuffles deck
        print(diamonds)
        # chooses one random item of list and removes it (saved in this variable)
        your_hand = random.choice(diamonds)
        hand.append(your_hand)  # adds variable your_hand to hand list
        print("This is your hand: ", hand)
        diamonds.remove(your_hand) #removes the your_hand card from diamonds
        print("Remaining cards on the Deck: ", diamonds)

if not diamonds:
    print("There are no more cards left on the deck")
