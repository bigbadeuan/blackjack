# BlackJack

import random

# THE PLANNING PHASE
# Player blackjack bool
player_blackjack = False
# Dealer cards
dealer_cards = []
# Player cards
player_cards = []

# Deal the cards
# Display the cards
# Dealer Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

# Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have ", player_cards)

# Sum of the Dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

# Sum of the Player cards

#while sum(player_cards) < 21:
#    action_taken = str(input("Do you want to stay or hit?  "))
#    if action_taken == "hit":
#        player_cards.append(random.randint(1, 11))
#        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
#    else:
#        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
#        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
#        while sum(dealer_cards) < 17:
#            dealer_cards.append(random.randint(1, 11))
#            print("The dealer hits and gets a " + str(dealer_cards[-1]) + " and now has a total of " + str(sum(dealer_cards)))
#        if sum(dealer_cards) > sum(player_cards) and sum(dealer_cards >= 21):
#            print("Dealer wins with " + str(sum(dealer_cards)))
#        else:
#            print("You win with " + str(sum(player_cards)))
#            break

#if sum(player_cards) > 21:
#    print("You BUSTED! Dealer wins.")
#elif sum(player_cards) == 21:
#    print("You have BLACKJACK! You Win!! 21")


while sum(player_cards) < 22:
    action = str(input("Would you like to stick or hit?  "))
    if action == "hit":
        player_cards.append(random.randint(1, 11))
        print("Your total is now equal to " + str(sum(player_cards)) + " from the following numbers ", player_cards)
        if sum(player_cards) == 21:
            player_blackjack == True
            print(" Congratulations! You have blackjack - hope the dealer doesn't get it!")
            break
    elif action == "stick":
        print("You have decided to stick on " + str(sum(player_cards)))
        time.sleep(1)
        print("The dealer has " + str(sum(dealer_cards)))
        time.sleep(1)
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.randint(1,11))
            print("the dealer hit and got a " + str(dealer_cards[-1]) + ", they now have a total of " + str(sum(dealer_cards)))
        if (sum(dealer_cards) >= 17 and sum(dealer_cards) <=21 and sum(player_cards) >=17 and sum(player_cards) <= 21):
           print("you have a total of " + str(sum(player_cards)))
           print("the dealer has a total of " + str(sum(dealer_cards)))
           if sum(dealer_cards) > sum(player_cards):
               print("player lose! the dealer has " + str(sum(dealer_cards)) + "and you have " + str(sum(player_cards)))
           elif sum(player_cards) > sum(dealer_cards):
               print("player wins! the player has " + str(sum(player_cards)) + "and the dealer has " + str(sum(dealer_cards)))
           else:
               print("it's a Tie! Dealer has " + str(sum(dealer_cards)) + "player has " + str(sum(player_cards)))     


if sum(player_cards > 21):
    print("You have bust the dealer wins no matter what the outcome is")

# Compare the sums of the cards between D v P
# If P card sum is greater than 21 = BUST
# If P card sum is less than 21 = Option Hit or Stay
# If P option Stay compare sum of D v P
# If P sum < 21 && > D sum then P wins!
# If P sum < D sum then P loses
