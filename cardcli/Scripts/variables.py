screen = None
window = None

class Game():
    scene = 'title'
    state = ''
    interaction = -1
    interaction_level = -1

class Cursor():
    menu = 0

class Camera():
    position = [-6, -40]

class Field():
    location = 'home'

    player_position = [1, 1]
    player_face = 'D'

class Player():
    inventory = []
    cards = []
    deck_1 = []
    deck_2 = []
    deck_3 = []

    life = 20
    level = 1
    tech = []

class Player_Battle():
    deck = []
    hand = []

class Battle():
    turn = 0
    play_mode = 'card'
    field = []
    player_grave = []
    enemy_grave= []
