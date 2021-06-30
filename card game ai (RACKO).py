'''''''''''''''
CS115, Project 3 Racko Game, Cole Watson
This program creates a game of Racko and allows you to choose the difficulty of your opponent.
Then it will play a game of Racko against you until one player wins.
'''''''''''''''
import sys
import random

#Define a global variable to denote the total number of cards.
numCards = 60 #9, 12, 60

#Define a global variable to denote the size of rack (number of cards in user's hand).
rackSize = 10 #3, 4, 10

def ask_difficulty():
    while True:
        print("*AI difficulty:*")
        print("Billy (Easy)")
        print("Joseph (Medium)")
        print("Rudy (Hard)")
        choice = input("Select opponent: ")
        choice = choice.lower()
        print()
        print("***Game Begins!***")
        print()
        if choice == 'easy' or choice == 'billy':
            return 1
        if choice == 'medium' or choice == 'joseph':
            return 2
        if choice == 'hard' or choice == 'rudy':
            return 3
        print("input error try again!")

def human_turn(human_hand, deck, discard_pile):
    # print lists corresponding to deck, discard pile and user hand
    # put into seperate function
    # print("Deck:")
    # print(deck)
    print("discard pile")
    print(discard_pile)
    print("your current hand:")
    print(human_hand)

    # Retrieve the top card in the discard pile and ask user if they want it
    top_discard = get_top_card(discard_pile)
    print("Do you want this discard card: " + str(top_discard))
    discard_pile_question = input("Enter yes or no: ")

    if discard_pile_question == 'yes':
        # Ask the user for the card (number) they want to kick out
        card_kick = int(input("Enter the number of the card you want to kick out: "))
        # Modify the user's hand and the discard pile
        find_and_replace(top_discard, card_kick, human_hand, discard_pile)
        # Print the user's hand
        print("your new hand is:")
        print(human_hand)
        print()
    elif discard_pile_question == "no":
        add_card_to_discard(top_discard, discard_pile)
        # Get the top card from deck and print it to show the user what they got
        top_card = get_top_card(deck)
        # Ask the user if they want this card
        print("The card you get from the deck is " + str(top_card))
        second_choice = input("Do you want to keep this card? Enter yes or no: ")
        if second_choice == 'yes':
            # Ask the user for the card (number) they want to kick out
            card_kick = input("Enter the number of the card you want to kick out: ")
            # Modify the user's hand and the discard pile
            find_and_replace(top_card, card_kick, human_hand, discard_pile)
        # Print the user's hand
        elif second_choice == 'no':
            # Add card to discard pile
            add_card_to_discard(top_card, discard_pile)
        # Print the user's hand
        print("your new hand is:")
        print(human_hand)
        print()
    else:
        print("Choice can be only yes or no.")
        sys.exit()

def deal_initial_hands(deck):
    human_hand = []
    computer_hand = []
    for i in range(rackSize):
        computer_hand.append(get_top_card(deck))
        human_hand.append(get_top_card(deck))
    return human_hand, computer_hand

def check_racko(hand):
    for i in range(len(hand) - 1):
        if hand[i] > hand[i + 1]:
            return False
    return True

def replaceDeck(card_stack):
    new_deck = shuffle(card_stack)
    new_discard = []
    return new_deck, new_discard


def shuffle(card_stack):
    random.shuffle(card_stack)
    return card_stack

def get_top_card(card_stack):
    t = card_stack[len(card_stack) - 1]
    card_stack.remove(t)
    return t


def add_card_to_discard(card, discard):
    discard.append(card)
    return
#racko ai here
def ai_racko(pile, original_hand):
    hand = original_hand[:]
    card = pile[len(pile) - 1]
    #checks for racko if card is taken
    for j in range(len(hand)):
        temp = hand[j]
        hand[j] = card
        nottrue = 0
        for i in range(len(hand) - 1):
            if hand[i] > hand[i + 1]:
                nottrue = 1
        hand[j] = temp
        if nottrue == 0:
            return True, j
    return False, None

def logic_racko(pile, original_hand):
    hand = original_hand[:]

    card = pile[len(pile) - 1]
    # checks for racko if card is taken
    for j in range(len(hand)):
        temp = hand[j]
        hand[j] = card
        nottrue = 0
        for i in range(len(hand) - 1):
            if hand[i] > hand[i + 1]:
                nottrue = 1
        hand[j] = temp
        if nottrue == 0:
            return True

def logic_ai(pile, original_hand):
    div = numCards // rackSize
    loc = (pile[-1] - 1) // div
    if (loc * 6) < original_hand[loc] and original_hand[loc] <= ((loc + 1) * 6):
        return False

    return True

def computer_logic(computer_hand, deck, discard):
#Define a variable to specify the numbers that can be "allotted" to a single card in the rack
    div = numCards // rackSize

    if logic_ai(discard, computer_hand) or ai_racko(discard, computer_hand) == True:
        # Show the discard card
        discard_card = get_top_card(discard)
        print("Computer: Chooses top discard card " + str(discard_card))

        #Choose a card to kick out
        #First determine index where discard_Card should be inserted.
        #Estimate it by dividing the discard Card with numbers per rack (div)
        loc = (discard_card - 1) // div

        #Replace by whatever card is in computer's hand at this index
        number_of_card = computer_hand[loc]
        print("Computer: Replacing it with  " + str(number_of_card))

        #Modify the discard pile and the computer's hand
        find_and_replace(discard_card, number_of_card, computer_hand, discard)
        print("Computer's new hand: ")
        print(computer_hand)

    else:
        # Pick the top card from deck and print it out
        deck_card = get_top_card(deck)
        #print("Computer: Chooses top card from the deck " + str(deck_card))

        coin = random.random()
        #Randomly decide whether to keep the deck card or not
        if logic_ai(discard, computer_hand) or ai_racko(discard, computer_hand) == True:
            # Choose a card to kick out
            # First determine index where deck card should be inserted.
            print("Computer: Chooses top deck card " + str(deck_card))

            loc = (deck_card - 1) // div
            # Replace by whatever card is in computer's hand at this index
            number_of_card = computer_hand[loc]
            print("Computer: Replacing it with " + str(number_of_card))

            #Modify the discard pile and the computer's hand
            find_and_replace(deck_card, number_of_card, computer_hand, discard)
            #print("Computer's new hand is:")
            #print(computer_hand)
        else:
            #print("Computer: Rejects top deck card " + str(deck_card))

            #Add card to discard pile
            add_card_to_discard(deck_card, discard)
            #print("Computer's new hand is:")
            #print(computer_hand)
            ...




def needed_card(pile, original_hand):#I dont know if this is useful this bot doesnt work very well
    hand = original_hand[:]
    hand2 = original_hand[:]
    hand3 = original_hand[:]
    card = pile[len(pile) - 1]
    #checks for racko if card is taken
    for j in range(len(hand)):
        temp = hand[j]
        hand[j] = card
        nottrue = 0
        for i in range(len(hand) - 1):
            if hand[i] > hand[i + 1]:
                nottrue = 1
        hand[j] = temp
        if nottrue == 0:
            return True, j

    #checks if useful for getting a racko

    for i in range(1,len(hand2) - 1):
        temp2 = hand2[i]
        hand2[i] = card
        if hand2[i - 1] < hand2[i] < hand2[i + 1]:
            return True, i
        hand[i] = temp2

    if card < hand3[0]:
        return True, 0

    if card > hand3[len(hand3) - 1]:
        return True, (len(hand3) - 1)

    return False, None



def find_and_replace(new_card, card_to_be_replaced, hand, discard):
    dex = hand.index(int(card_to_be_replaced))
    hand[dex] = new_card
    #hand.replace(str(card_to_be_replaced), new_card)
    discard.append(int(card_to_be_replaced))
    return

def computer_medium(computer_hand, deck, discard):
#Define a variable to specify the numbers that can be "allotted" to a single card in the rack
    div = numCards // rackSize

    #print lists corresponding to deck, discard pile and computer's current hand
    print("deck:")
    print(deck)
    print("discard pile:")
    print(discard)
    print()
    print("computer's current hand:")
    print(computer_hand)

    #randomly decide whether to choose from the discard pile or deck
    coin = random.random() #import random for this to work
    if coin > 0.5:
        # Show the discard card
        discard_card = get_top_card(discard)
        print("Computer: Chooses top discard card " + str(discard_card))

        #Choose a card to kick out
        #First determine index where discard_Card should be inserted.
        #Estimate it by dividing the discard Card with numbers per rack (div)
        loc = (discard_card - 1) // div

        #Replace by whatever card is in computer's hand at this index
        number_of_card = computer_hand[loc]
        print("Computer: Replacing it with  " + str(number_of_card))

        #Modify the discard pile and the computer's hand
        find_and_replace(discard_card, number_of_card, computer_hand, discard)
        print("Computer's new hand: ")
        print(computer_hand)

    else:
        # Pick the top card from deck and print it out
        deck_card = get_top_card(deck)
        print("Computer: Chooses top card from the deck " + str(deck_card))

        coin = random.random()
        #Randomly decide whether to keep the deck card or not
        if coin > 0.5:
            # Choose a card to kick out
            # First determine index where deck card should be inserted.
            print("Computer: Chooses top deck card " + str(deck_card))

            loc = (deck_card - 1) // div
            # Replace by whatever card is in computer's hand at this index
            number_of_card = computer_hand[loc]
            print("Computer: Replacing it with " + str(number_of_card))

            #Modify the discard pile and the computer's hand
            find_and_replace(deck_card, number_of_card, computer_hand, discard)
            print("Computer's new hand is:")
            print(computer_hand)
        else:
            print("Computer: Rejects top deck card " + str(deck_card))

            #Add card to discard pile
            add_card_to_discard(deck_card, discard)
            print("Computer's new hand is:")
            print(computer_hand)
            ...

def computer_easy(computer_hand, deck, discard):
#Define a variable to specify the numbers that can be "allotted" to a single card in the rack
    #div = numCards // rackSize

    #print lists corresponding to deck, discard pile and computer's current hand
    print("deck:")
    print(deck)
    print("discard pile:")
    print(discard)
    print()
    print("computer's current hand:")
    print(computer_hand)

    #checks using ai to see if it should pick up the discard card
    take_discard, lineno = needed_card(discard, computer_hand)

    if take_discard is True:
        # Show the discard card
        discard_card = get_top_card(discard)
        print("Computer: Chooses top discard card " + str(discard_card))

        #Choose a card to kick out
        #First determine index where discard_Card should be inserted.

        #Replace by whatever card is in computer's hand at this index
        number_of_card = computer_hand[lineno]
        print("Computer: Replacing it with  " + str(number_of_card))

        #Modify the discard pile and the computer's hand
        find_and_replace(discard_card, number_of_card, computer_hand, discard)
        print("Computer's new hand: ")
        print(computer_hand)

    else:
        take_deck, lineno = needed_card(deck, computer_hand)
        # Pick the top card from deck and print it out
        deck_card = get_top_card(deck)
        print("Computer: Chooses top card from the deck " + str(deck_card))

        #
        if take_deck is True:
            # Choose a card to kick out
            # First determine index where deck card should be inserted.
            print("Computer: Chooses top deck card " + str(deck_card))

            # Replace by whatever card is in computer's hand at this index
            number_of_card = computer_hand[lineno]
            print("Computer: Replacing it with " + str(number_of_card))

            #Modify the discard pile and the computer's hand
            find_and_replace(deck_card, number_of_card, computer_hand, discard)
            print("Computer's new hand is:")
            print(computer_hand)
        else:
            print("Computer: Rejects top deck card " + str(deck_card))

            #Add card to discard pile
            add_card_to_discard(deck_card, discard)
            print("Computer's new hand is:")
            print(computer_hand)
            ...


def main():
    difficulty = ask_difficulty()
    # create a list of integers that represents a deck
    #random.seed(26)
    deck = []
    for i in range(numCards):
        deck.append(i + 1)
    #shuffle deck
    shuffle(deck)
    # Assign hand to the user
    human_hand, computer_hand = deal_initial_hands(deck)


    # create an empty discard pile
    discard_pile = []
    # Take out top card from the deck to begin the discard pile
    topcard = get_top_card(deck)
    add_card_to_discard(topcard, discard_pile)



    while check_racko(human_hand) == False and check_racko(computer_hand) == False:
        # print lists corresponding to deck, discard pile and user hand
        #put into seperate function
        #print("Deck:")
        #print(deck)
        print("discard pile")
        print(discard_pile)
        print("your current hand:")
        print(human_hand)
        human_turn(human_hand, deck, discard_pile)

        if len(deck) == 0:
            print("User: WOAH! Deck is empty. Shuffling discard pile and using that as the new deck.")
            deck, discard_pile = replaceDeck(discard_pile)
            discard_pile = [get_top_card(deck)]

        if check_racko(human_hand) == False:
            if difficulty == 1:
                computer_easy(computer_hand, deck, discard_pile)
            elif difficulty == 2:
                computer_medium(computer_hand, deck, discard_pile)
            elif difficulty == 3:
                computer_logic(computer_hand, deck, discard_pile)

        if len(deck) == 0:
            print("Computer: WOAH! Deck is empty. Shuffling discard pile and using that as the new deck.")
            deck, discard_pile = replaceDeck(discard_pile)
            discard_pile = [get_top_card(deck)]

    if check_racko(computer_hand) == True:
        print("COMPUTER WINS! with hand of " + str(computer_hand) + ".")
    if check_racko(human_hand) == True:
        print("HUMAN WINS! with hand of " + str(human_hand) + ".")
main()