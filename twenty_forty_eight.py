"""
Clone of 2048 game.
"""

import random
try:
    import poc_2048_gui
except ImportError:
    print("import poc_2048_gui failed. ignoring error.")

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def slide(line):
    """
    function that slides a single row or column towards the 0 index,
    without merging/summing any numbers
    :param line: input list
    :return: returns list that has been slid
    """
    # start with as many 0's as there are elements in line
    slid_list = [0 for _num in range(len(line))]
    # iterate over line looking for non-zero entries, adding it
    # to the merged_list
    non_zeroes = 0
    for index in range(len(line)):
        if line[index] != 0:
            slid_list[non_zeroes] = line[index]
            non_zeroes += 1
    return slid_list


def pair(line):
    """
    function that pairs a single row or column: e.g. of the adjacent
    pair, the lower index has their sum and the higher index has a 0
    :param line: input list (has to take even length tiles
    :return: returns list that has been paired
    """
    # iterate over index / 2
    paired_list = list(line)
    for index in range(len(line) - 1):
        lower_index = index
        upper_index = index + 1
        if paired_list[lower_index] == paired_list[upper_index]:
            paired_list[lower_index] = (paired_list[lower_index] + paired_list[upper_index])
            paired_list[upper_index] = 0
    return paired_list


def merge(line):
    """
    function that merges single row or column for the game 2048
    :param line: input list
    :return: returns merged list
    """
    # 1. slide towards 0 index
    slid_line = slide(line)
#    print("1. slid line is", slid_line)
    # 2. pair values
    paired_line = pair(slid_line)
#    print("2. paired line is", paired_line)
    # 3. slide again
    merged_list = slide(paired_line)
    return merged_list


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height_ = grid_height
        self._grid_width_ = grid_width
        # replace with your code
        self._grid_ = []
        # grid_occupied places a one where there is a value and 0 otherwise
        self._grid_occupied_ = []
        # initial index mapping
        up_index = [(0, col) for col in range(self._grid_width_)]
        down_index = [(self._grid_height_ - 1, col) for col in range(self._grid_width_)]
        left_index = [(row, 0) for row in range(self._grid_height_)]
        right_index = [(row, self._grid_width_ - 1) for row in range(self._grid_height_)]

        self._initial_index_ = {1: up_index, 2: down_index, 3: left_index, 4: right_index}
        self._initial_index_len_ = {1: self._grid_height_, 2: self._grid_height_,
                                    3: self._grid_width_, 4: self._grid_width_}

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        print("RESET!")
        self._grid_ = []
        for _ in range(self._grid_height_):
            self._grid_.append([0 for _ in range(self._grid_width_)])
            self._grid_occupied_.append([0 for _ in range(self._grid_width_)])
        self.new_tile()
        self.new_tile()
        print("initialised", self)
        print("")

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        output = "current grid (" + str(self._grid_height_) + " x " + str(
                self._grid_width_) + "):"
        for row in range(self._grid_height_):
            output += "\n" + str(self._grid_[row])
        return output

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height_

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width_

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved. Takes numeric input (1, 2, 3, 4)
        is (up, down, left, right)
        """
        # create list for each index
        initial_tiles = self._initial_index_[direction]
        index_len = self._initial_index_len_[direction]
        offsets = OFFSETS[direction]
        tiles_moved = 0

        print("\n MOVE", direction, initial_tiles)
        print(self)
        for initial_tile in initial_tiles:
            print("initial_tile is", initial_tile)
            temp_list = []
            tile_index = [initial_tile[0], initial_tile[1]]
            for temp_list_index in range(index_len):
                tile = self.get_tile(tile_index[0], tile_index[1])
                temp_list.append(tile)
                tile_index[0] += offsets[0]
                tile_index[1] += offsets[1]
            print("unmerged", temp_list)
            temp_list_merged = merge(temp_list)
            print("merged", temp_list_merged)

            # setting merged list back as tiles
            tile_index = [initial_tile[0], initial_tile[1]]
            for temp_list_index in range(index_len):
                # add tiles moved counter
                if self.get_tile(tile_index[0], tile_index[1]) != temp_list_merged[temp_list_index]:
                    tiles_moved += 1
                self.set_tile(tile_index[0], tile_index[1], temp_list_merged[temp_list_index])
                tile_index[0] += offsets[0]
                tile_index[1] += offsets[1]
            print(self)
            print("")

        print("tiles_moved", tiles_moved)
        if tiles_moved > 0:
            print("tiles moved - NEW TILE")
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        max_tries = 1000
        tries = 0
        total_tiles = self._grid_height_ * self._grid_width_

        grid_occupied_total = 0
        for row in range(self._grid_height_):
            for col in range(self._grid_width_):
                if self._grid_[row][col] > 0:
                    grid_occupied_total += 1

        print("trying to add new tile...")
        print("grid_occupied_total", grid_occupied_total)

        # if there is empty space:
        if grid_occupied_total < total_tiles:
            random_row = random.randrange(0, self._grid_height_)
            random_col = random.randrange(0, self._grid_width_)

            # find random grid cell to place tile
            while self._grid_[random_row][random_col] != 0 and tries <= max_tries:
                random_row = random.randrange(0, self._grid_height_)
                random_col = random.randrange(0, self._grid_width_)
                tries += 1

            if tries >= max_tries:
                print("ERROR max_tries")

            # create random tile
            if random.randrange(10) < 9:
                random_tile = 2
            else:
                random_tile = 4

            print("random_tile is", random_tile, "to be inserted at", "row:",
                  random_row, "col", random_col)

            self._grid_[random_row][random_col] = random_tile
            self._grid_occupied_[random_row][random_col] = 1

        else:
            print("nowhere left to place tiles!")

        print(self)
        print("")

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid_[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid_[row][col]

try:
    poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
except NameError:
    print("poc_2048_gui not imported. ignoring error...")
