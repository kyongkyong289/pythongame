import variables as var
import carddata as cards

def deck_generate_battle(mode):
    var.Player_Battle.deck = []

    if mode == 'adventure':
        for i in range(len(var.Player.deck_1)):
            for j in range(var.Player.deck_1[i][2]):
                tempID = var.Player.deck_1[i][0]
                var.Player_Battle.deck.append({'ID' : tempID,
                                               'type' : cards[tempID]['type'],
                                               'element' : cards[tempID]['element'],
                                               'rarity' : cards[tempID]['rarity'],
                                               'name' : cards[tempID]['name'],
                                               'energy' : cards[tempID]['energy'],
                                               'attack' : cards[tempID]['attack'],
                                               'life' : cards[tempID]['life'],
                                               'special' : cards[tempID]['special'],
                                               'play' : [cards[tempID]['play'][0], cards[tempID]['play'][1], cards[tempID]['play'][2]]})

def draw_from_deck():
    if len(var.Player_Battle.deck) > 0:
        temp_card = var.Player_Battle.deck.pop()

        if len(var.Player_Battle.hand < 8):
            var.Player_Battle.hand.apped(temp_card)

def start_hand_change():
    if len(var.Player_Battle.deck) > 5:
        for i in range(3):
            if var.Player_Battle.hand_change[i] === True:
                temp = var.Player_Battle.deck[i]
                var.Player_Battle.deck[i] = var.Player_Battle.deck[i + 3]
                var.Player_Battle.deck[i + 3] = temp