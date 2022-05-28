#linear(brute force) search:
#consider list of cards in decreasing order, return index of specific value
cards = [13, 11, 7, 10, 7, 4, 3, 1, 0]
#query= (input ("select a number between 0 and 13: "))

def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            print ("Your query is found in index: ", position)
            break
        else:
            position +=1
    if position == len(cards):
        print("Sorry, we couldn't find your card and you ran out of cards")
            
            
            
locate_card(cards, 4)
   
