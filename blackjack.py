import random

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

card_list = list(cards.keys())

game = True
def pick_card():
    card = random.choice(card_list)
    return card

# Initial game setup
dealer = []
player = []
dealer_card = pick_card()
player_card = pick_card()
dealer_card2 = pick_card()
player_card2 = pick_card()
print('Dealer draws: %s' % dealer_card)
print('Player draws: ' + player_card + ' and ' + player_card2)
dealer.append(cards[dealer_card])
dealer.append(cards[dealer_card2])
player.append(cards[player_card])
player.append(cards[player_card2])
print('Player showing: ', sum(player))

# Game logic that inteacts with player
while(game):
    if sum(dealer) != 21 and sum(player) != 21:
        hit = input('Player hits? (y/n) ')
        if hit == 'y':
            player_card = pick_card()
            player.append(cards[player_card])
            print('Player draws: ', player_card)
            print('Player showing: ', sum(player))
            if sum(player) > 21:
                if 11 in player:
                    player.remove(11)
                    player.append(1)
                    print('Switching Ace value to 1')
                    print('Player showing: ', sum(player))
                else:
                    print('Player busts. Dealer wins')
                    break
            elif sum(player) == 21:
                print('Blackjack! Player wins!')
                break
        elif hit == 'n':
            if sum(player) > sum(dealer):
                print("Dealer's 2nd card: %s" % dealer_card2)
                print('Dealer showing: ', sum(dealer))
                while(sum(dealer) < sum(player) and sum(dealer) < 21):
                    dealer_card = pick_card()
                    print('Dealer draws: %s' % dealer_card)
                    dealer.append(cards[dealer_card])
                    print('Dealer showing: ', sum(dealer))
                    if sum(dealer) > 21:
                        if 11 in dealer:
                            dealer.remove(11)
                            dealer.append(1)
                            print('Switching Ace value to 1')
                            print('Dealer showing: ', sum(dealer))
                        else:
                            print('Dealer busts. Player wins!')
                            game = False
                    elif sum(dealer) == 21:
                        print('Blackjack! Dealer wins')
                        game = False
                    elif sum(dealer) >= sum(player):
                        print('Dealer wins')
                        game = False
        else:
            print('Invalid input. Try again')

    else: # This runs when dealer/player get initial blackjack
        if sum(dealer) == 21:
            print("Dealer's 2nd card: %s" % dealer_card2)
            print('Blackjack! Dealer wins')
            game = False
        else:
            print('Blackjack! Player wins!')
            game = False
