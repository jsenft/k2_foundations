import random

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': (1, 11)}

card_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

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


#hit = input('Player hits? y/n')
#if hit == 'y' or 'Y':
#    player_card = pick_card()
