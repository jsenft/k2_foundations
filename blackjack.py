import random

cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

card_list = list(cards.keys())
game = True

def pick_card():
    card = random.choice(card_list)
    return card

def total_cards(cards):
    if sum(cards) > 21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
    return sum(cards)

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
player_score = total_cards(player)
dealer_score = total_cards(dealer)
print('Player showing: ', player_score)

while(game):
    if player_score < 21:
        hit = input('Player hits? (y/N) ')
        if hit != 'y':
            if player_score >= dealer_score:
                print("Dealer's 2nd card: %s" % dealer_card2)
                print('Dealer showing: ', dealer_score)
                while(dealer_score <= player_score or dealer_score > 17 and dealer_score < 21):
                    dealer_card = pick_card()
                    print('Dealer draws: %s' % dealer_card)
                    dealer.append(cards[dealer_card])
                    dealer_score = total_cards(dealer)
                    print('Dealer showing: ', dealer_score)
                    if dealer_score > 21:
                        print('Dealer busts. Player wins!')
                        game = False
                        break
                    elif dealer_score > player_score:
                        print('Dealer wins')
                        game = False
                        break
                    elif dealer_score < player_score:
                        print('Player wins')
                        game = False
                        break
                    elif dealer_score == player_score:
                        print('Game is a push')
                        game = False
                        break
            else:
                print("Dealer's 2nd card: %s" % dealer_card2)
                print('Dealer showing: ', dealer_score)
                if dealer_score < player_score:
                    print('Player wins!')
                    game = False
                    break
                elif dealer_score > player_score:
                    print('Dealer wins')
                    game = False
                    break
                else:
                    print('Game is a push')
                    game = False
                    break

        else:
            player_card = pick_card()
            player.append(cards[player_card])
            player_score = total_cards(player)
            print('Player draws: ', player_card)
            print('Player showing: ', player_score)

    elif player_score == 21:
        print("Dealer's 2nd card: %s" % dealer_card2)
        print('Dealer showing: ', dealer_score)
        while(dealer_score <= player_score or dealer_score > 17 and dealer_score < 21):
            dealer_card = pick_card()
            print('Dealer draws: %s' % dealer_card)
            dealer.append(cards[dealer_card])
            dealer_score = total_cards(dealer)
            print('Dealer showing: ', dealer_score)
            if dealer_score > 21:
                print('Dealer busts. Player wins!')
                game = False
                break
            elif dealer_score > player_score:
                print('Dealer wins')
                game = False
                break
            elif dealer_score < player_score:
                print('Player wins')
                game = False
                break
            elif dealer_score == player_score:
                print('Game is a push')
                game = False
                break
