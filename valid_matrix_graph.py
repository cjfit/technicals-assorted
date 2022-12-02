"""
Given a set of coordinates, return a set with tuples of valid coordinates.
The coordinates are valid if the player can move in all four directions and not hit a wall (-1) or edge (out of the matrix bounds)
"""

board = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

def game(pos):
    """
    Given a position, return the spaces that the player can move to
    """
    rows = len(board)
    cols = len(board[0])

    # Get list of directions
    # Directions represent spaces to move to
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # Return_Set
    return_set = set()

    for xval, yval in directions:
        x_move = pos[0] + xval
        y_move = pos[1] + yval

        # Check within bounds
        if x_move < 0 or x_move > rows - 1:
            continue
        if y_move < 0 or y_move > cols -1:
            continue

        # Check value is not equal to -1 (wall)
        if board[x_move][y_move] == -1:
            continue



        return_set.add((x_move, y_move))

    return return_set

print(game(start1))
print(game(start2))
print(game(start3))
print(game(start4))
print(game(start5))
print(game(start6))
print(game(start7))
