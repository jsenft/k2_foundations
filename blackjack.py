import random

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': (1, 11)}

card_list = list(cards.keys())

game = True
def pick_card():
    card = random.choice(card_list)
    return card

dealer = []
player = []
dealer_card = pick_card()
player_card = pick_card()
dealer_card2 = pick_card()
player_card2 = pick_card()
print('Dealer draws: %s' % dealer_card)
print('Player draws: ' + player_card + ' and ' + player_card2)

def add_values(card, values):
    if sum(values)  <= 10:
        if card == 'A':
            values.append(cards['A'][1])
        else:
            values.append(cards[card])
    else:
        if card == 'A':
            values.append(cards['A'][0])
        else:
            values.append(cards[card])

add_values(dealer_card, dealer)
add_values(dealer_card2, dealer)
add_values(player_card, player)
add_values(player_card2, player)
print('Player showing: ', sum(player))
while(game):
    if sum(dealer) != 21 and sum(player) != 21:
        hit = input('Player hits? (y/n) ')
        if hit == 'y':
            player_card = pick_card()
            add_values(player_card, player)
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
                    add_values(dealer_card, dealer)
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

    else:
        if sum(dealer) == 21:
            print("Dealer's 2nd card: %s" % dealer_card2)
            print('Blackjack! Dealer wins')
            game = False
        else:
            print('Blackjack! Player wins!')
            game = False
