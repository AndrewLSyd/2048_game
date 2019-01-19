"""
GUI implementation of twenty forty eight game.
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import twenty_forty_eight

# global variables

my_board = twenty_forty_eight.TwentyFortyEight(3, 3)

# define event handlers


# create frame and add a button and labels
frame = simplegui.create_frame("2048", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turn_counter))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

