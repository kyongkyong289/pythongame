screen = None

class Inputs():
    class Mouse():
        lx = 0
        ly = 0

class Game():
    scene = 'title'
    state = ''

class Shop():
    level = 1
    exp = [0, 3]

    reroll_cost = 2
    upgrade_cost = 8
    lock_cost = 0

class Player():
    coin = 6
    coin_max = 6
    life = 60
    life_max = 60