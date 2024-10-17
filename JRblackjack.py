import random
def deal_cards():
    cards=[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    card=random.choice(cards)
    return card

def calc_count(hand):
    count=0
    aces=0
    for card in hand:
        if card in ["J", "Q", "K"]:
            count=count+10
        elif card=="A":
            aces=aces+1
            count=count+11
        else:
            count=count+card
    while count>21 and aces:
        count=count-10
        aces=aces-1
    return count

def play():
    player_hand=[deal_cards(), deal_cards()]
    dealer_hand=[deal_cards(), deal_cards()]
    print()
    print("Welcome to the BlackJack table!")
    print()
    print("Your Cards:", player_hand, "Current Count:", calc_count(player_hand))
    print("Dealer's First Card:", dealer_hand[0])
    print()
    while calc_count(player_hand)<21:
        hs=input("Type 'h' to hit or 's' to stand: ")
        if hs=="h":
            player_hand.append(deal_cards())
            print()
            print("Your Cards:", player_hand, "New Count:", calc_count(player_hand))
            dealer_hand.append(deal_cards())
        else:
            break
    print()
    print("Your Final Hand:", player_hand, "Final Count:", calc_count(player_hand))
    print("Dealer's Final Hand:", dealer_hand, "Final Count:", calc_count(dealer_hand))
    if calc_count(player_hand)>21:
        print("Player Bust! Dealer Wins! :(")
    elif calc_count(dealer_hand)>21:
        print("Dealer Bust! You Win! :)")
    elif calc_count(player_hand)>calc_count(dealer_hand):
        print("You Win! :)")
    elif calc_count(player_hand)<calc_count(dealer_hand):
        print("Dealer Wins! :(")
    elif calc_count(player_hand)==21:
        if calc_count(dealer_hand)==21:
            print("Its a Push!")
        else:
            print("BlackJack! You Win!")
    else:
        print("Its a Draw!")
    print()
    print("Thank You for Playing!")
    print()

play()