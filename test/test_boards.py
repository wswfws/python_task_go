board3x3 = [
    ['.', '.', '.'],
    ['.', 'B', '.'],
    ['.', '.', 'W']
]

board3x3_one_empty = [
    ['B', 'B', 'B'],
    ['.', 'B', 'B'],
    ['.', 'W', 'W']
]

board9x9_1 = [
    ['.', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'W', 'W'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'B', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'B', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'B', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
]

board9x9_2 = [
    ['B', 'B', '.', '.', '.', 'W', 'W', 'W', '.'],
    ['B', 'B', 'B', '.', '.', 'W', 'W', 'W', '.'],
    ['B', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'W', 'W', 'W', '.', '.', '.'],
    ['.', '.', '.', 'W', 'W', 'W', '.', '.', '.'],
    ['.', '.', '.', 'W', '.', '.', '.', 'B', 'B'],
    ['.', '.', '.', '.', '.', '.', 'B', 'B', 'B'],
    ['W', 'W', '.', '.', '.', '.', 'B', '.', 'B'],
    ['W', 'W', 'W', '.', '.', '.', 'B', 'B', 'B']
]

board9x9_empty_holes = [
    ['.', 'B', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'B', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'W', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'B', 'B'],
    ['.', '.', '.', '.', '.', '.', 'B', '.', 'B'],
    ['.', '.', '.', '.', '.', '.', 'B', '.', 'B'],
    ['.', '.', '.', '.', '.', '.', 'B', 'B', 'B']
]

board9x9_captured_easy = [
    ['.', 'B', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'W'],
    ['.', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'W']
]

board9x9_captured_easy_neg = [
    ['.', 'W', '.', '.', '.', '.', '.', '.', '.'],
    ['W', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.', '.', '.', '.', '.', 'B', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'B']
]

board9x9_captured_hard = [
    ['.', 'B', '.', '.', '.', 'B', '.', '.', 'B'],
    ['.', 'B', '.', '.', '.', '.', 'B', 'B', '.'],
    ['B', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.', 'W', 'W', 'W', '.', '.', '.'],
    ['.', '.', '.', 'W', '.', 'W', '.', '.', '.'],
    ['W', '.', '.', '.', 'W', '.', '.', 'B', 'B'],
    ['.', 'W', '.', '.', '.', '.', 'B', '.', 'B'],
    ['W', 'W', '.', '.', '.', '.', 'B', '.', 'B'],
    ['.', '.', '.', '.', '.', '.', 'B', 'B', 'B']
]

board_captured_one_circle = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'B', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'B', 'B', '.', '.', '.', '.'],
    ['.', '.', '.', 'B', 'W', 'B', '.', '.', '.'],
    ['.', '.', '.', '.', 'B', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'W', '.']
]

board13x13_captured = [
    ['.', '.', '.', '.', 'W', '.', '.', 'W', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'W', 'W', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'W', '.', '.', 'W', '.', 'B'],
    ['.', '.', '.', '.', '.', '.', '.', 'W', '.', 'W', '.', 'B', '.']
]

board19x19_captured = [
    ['.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['W', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['W', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', 'B'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', 'B', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', 'B', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', 'B', '.', '.', '.', '.', '.', '.']
]


# board_empty_grid = [
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.']
# ]

# [['.'] * 9 for _ in range(9)]
