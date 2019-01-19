"""
2048 row merge function
"""


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




