class Main():
    title_text = [1, 2]
    dialogue = [21, 2, 7, 92]
    dialogue_text = [23, 4] 

class Menu():
    new_game = [4, 4]
    load_game = [6, 4]
    dungeon = [8, 4]

    cursor = [[4, 2], [6, 2], [8, 2]]

class Field():
    cell_size = [5, 6]
    cell_interval = [4, 5]

class Battle():
    player_hero = [3, 36, 16, 10]
    player_units = [[3, 54], [8, 54], [13, 54], [3, 45], [8, 45], [13, 45]]
    enemy_hero = [3, 81, 16, 10]
    enemy_units = [[3, 72], [8, 72], [13, 72], [3, 63], [8, 63], [13, 63]]
    cell_size = [6, 10]

    info_1 = [25, 40]
    info_2 = [26, 40]

    class Start_Window():
        rect = [6, 10, 18, 76]

        start_hand_cursors = [[8, 12], [10, 12], [12, 12], [14, 12]]
        start_hand_blink = [[8, 13], [10, 13], [12, 13]]
        start_hand_text = [[8, 14], [10, 14], [12, 14]]

        start_text = [14, 14]