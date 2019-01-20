"""
GUI implementation of twenty forty eight game.
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import twenty_forty_eight
import math

#  __      _____ _       _           _
# /_ |    / ____| |     | |         | |
#  | |   | |  __| | ___ | |__   __ _| |___
#  | |   | | |_ | |/ _ \| '_ \ / _` | / __|
#  | |_  | |__| | | (_) | |_) | (_| | \__ \
#  |_(_)  \_____|_|\___/|_.__/ \__,_|_|___/
WIDTH = 600
HEIGHT = 600
GRID_ROWS = 4
GRID_COLS = 4

my_board = twenty_forty_eight.TwentyFortyEight(GRID_ROWS, GRID_COLS)

#  ___      _    _      _                    __                  _   _
# |__ \    | |  | |    | |                  / _|                | | (_)
#    ) |   | |__| | ___| |_ __   ___ _ __  | |_ _   _ _ __   ___| |_ _  ___  _ __  ___
#   / /    |  __  |/ _ \ | '_ \ / _ \ '__| |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#  / /_ _  | |  | |  __/ | |_) |  __/ |    | | | |_| | | | | (__| |_| | (_) | | | \__ \
# |____(_) |_|  |_|\___|_| .__/ \___|_|    |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#                        | |
#                        |_|
#  _  _     _____        __   ______               _     _    _                 _ _
# | || |   |  __ \      / _| |  ____|             | |   | |  | |               | | |
# | || |_  | |  | | ___| |_  | |____   _____ _ __ | |_  | |__| | __ _ _ __   __| | | ___ _ __ ___
# |__   _| | |  | |/ _ \  _| |  __\ \ / / _ \ '_ \| __| |  __  |/ _` | '_ \ / _` | |/ _ \ '__/ __|
#    | |_  | |__| |  __/ |   | |___\ V /  __/ | | | |_  | |  | | (_| | | | | (_| | |  __/ |  \__ \
#    |_(_) |_____/ \___|_|   |______\_/ \___|_| |_|\__| |_|  |_|\__,_|_| |_|\__,_|_|\___|_|  |___/
def new_game():
    my_board.reset()


def draw(canvas):
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            tile_val = my_board.get_tile(row, col)
            col_val = min(255, int(math.log2(tile_val + 1) * 40))
            canvas.draw_text(str(my_board.get_tile(row, col)), [WIDTH / GRID_COLS * (col + 0.45),
                                                                HEIGHT / GRID_ROWS * (row + 0.6)],
                             100, "rgb(" + str(col_val) + ", " + str("0") + ", " + str(255 - col_val) + ")")
    label.set_text("Score = " + str(my_board.get_score()))

# keyboard handler
keydown_inputs = {simplegui.KEY_MAP["up"]: 1, simplegui.KEY_MAP["down"]: 2,
                  simplegui.KEY_MAP["left"]: 3, simplegui.KEY_MAP["right"]: 4}


def keydown_handler(key):
    try:
        print(keydown_inputs[key])
        my_board.move(keydown_inputs[key])
        print("score", my_board.get_score())
    except KeyError:
        print("invalid key")


# create frame and add a button and labels
frame = simplegui.create_frame("2048", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)

#    __     _____            _     _              ______               _
#   / /    |  __ \          (_)   | |            |  ____|             | |
#  / /_    | |__) |___  __ _ _ ___| |_ ___ _ __  | |____   _____ _ __ | |_
# | '_ \   |  _  // _ \/ _` | / __| __/ _ \ '__| |  __\ \ / / _ \ '_ \| __|
# | (_) |  | | \ \  __/ (_| | \__ \ ||  __/ |    | |___\ V /  __/ | | | |_
#  \___(_) |_|  \_\___|\__, |_|___/\__\___|_|    |______\_/ \___|_| |_|\__|
#          | |  | |     __/ |     | | |
#          | |__| | __ |___/_   __| | | ___ _ __ ___
#          |  __  |/ _` | '_ \ / _` | |/ _ \ '__/ __|
#          | |  | | (_| | | | | (_| | |  __/ |  \__ \
#          |_|  |_|\__,_|_| |_|\__,_|_|\___|_|  |___/
frame.set_keydown_handler(keydown_handler)
frame.set_draw_handler(draw)
frame.set_canvas_background("white")
frame.add_label("")
frame.add_label("Welcome to 2048!")
frame.add_label("")
frame.add_label("Use the arrow keys to slide the tiles.")
frame.add_label("")
label = frame.add_label("Score = " + str(my_board.get_score()))


#  ______    _____ _             _      __
# |____  |  / ____| |           | |    / _|
#     / /  | (___ | |_ __ _ _ __| |_  | |_ _ __ __ _ _ __ ___   ___
#    / /    \___ \| __/ _` | '__| __| |  _| '__/ _` | '_ ` _ \ / _ \
#   / /     ____) | || (_| | |  | |_  | | | | | (_| | | | | | |  __/
#  /_(_)   |_____/ \__\__,_|_|  _\__| |_| |_|  \__,_|_| |_| |_|\___|
#                          | | | | (_)
#            __ _ _ __   __| | | |_ _ _ __ ___   ___ _ __ ___
#           / _` | '_ \ / _` | | __| | '_ ` _ \ / _ \ '__/ __|
#          | (_| | | | | (_| | | |_| | | | | | |  __/ |  \__ \
#           \__,_|_| |_|\__,_|  \__|_|_| |_| |_|\___|_|  |___/

new_game()
frame.start()

