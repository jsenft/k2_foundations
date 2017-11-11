import random

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': (1, 11)}

card_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

dealer = []
player = []
game = True

def pick_card():
    card = random.choice(card_list)
    return card

dealer_card = pick_card()
player_card = pick_card()

while(game):
    if sum(dealer)  <=10:
        if dealer_card == 'A':
            dealer.append(cards[dealer_card][1])
        else:
            dealer.append(cards[dealer_card])
    else:
        if dealer_card == 'A':
            dealer.append(cards[dealer_card][0])
        else:
            dealer.append(cards[dealer_card])

    if sum(player) <= 10:
        if player_card == 'A':
            player.append(cards[player_card][1])
        else:
            player.append(cards[player_card])
    else:
        if player_card == 'A':
            player.append(cards[player_card][0])
        else:
            player.append(cards[player_card])

    print('Dealer draws: ', dealer_card)
    print('Dealer total: ', sum(dealer))
    print('Player draws: ', player_card)
    print('Player total: ', sum(player))
    game = False

    #hit = input('Player hits? y/n')
    #if hit == 'y' or 'Y':
    #    player_card = pick_card()
