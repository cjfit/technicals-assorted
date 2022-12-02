'''

Given a board and an end position for the player, write a function to determine if it is possible to travel from every open cell on the board to the given end position.

board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

board2 = [
    [  0,  0,  0, 0, -1 ],
    [  0, -1, -1, 0,  0 ],
    [  0,  0,  0, 0,  0 ],
    [ -1, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
]

board3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]

board4 = [
    [0,  0,  0,  0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0,  0,  0,  0, 0],
]

board5 = [
    [0],
]

end1 = (0, 0)
end2 = (5, 0)

Expected output:

isReachable(board1, end1) -> True
isReachable(board1, end2) -> True
isReachable(board2, end1) -> False
isReachable(board2, end2) -> False
isReachable(board3, end1) -> False
isReachable(board4, end1) -> True
isReachable(board5, end1) -> True


n: width of the input board
m: height of the input board

'''

board1 = [
    [0, 0, 0, 0, -1],
    [0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

board2 = [
    [0, 0, 0, 0, -1],
    [0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [-1, -1, 0, 0, 0],
    [0, -1, 0, 0, 0],
    [0, -1, 0, 0, 0],
]

board3 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, -1, -1, -1, -1, -1, 0],
    [0, -1, 0, 0, 0, -1, 0],
    [0, -1, 0, 0, 0, -1, 0],
    [0, -1, 0, 0, 0, -1, 0],
    [0, -1, -1, -1, -1, -1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

board4 = [
    [0, 0, 0, 0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 0],
]

board5 = [
    [0],
]

end1 = (0, 0)
end2 = (5, 0)

import collections


def find_path(board, end):
    """
    Given a path and a board, determine if all open cells have a path there
    """

    # Get Length of Rows and Cols
    rows = len(board)
    cols = len(board[0])

    def bfs(original_pos, visit):

        visit.add(original_pos)
        q = collections.deque()
        q.append(original_pos)

        while q:
            pos = q.pop()
            # Return True if found
            if pos == end:
                return True

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for x_val, y_val in directions:

                new_pos = (pos[0] + x_val, pos[1] + y_val)

                # Check if been visited
                if new_pos in visit:
                    continue

                visit.add(new_pos)

                # Check within bounds (not outside the grid)
                if new_pos[0] < 0 or new_pos[0] > rows - 1:
                    continue
                if new_pos[1] < 0 or new_pos[1] > cols - 1:
                    continue

                # Check not blocked (-1)
                if board[new_pos[0]][new_pos[1]] == -1:
                    continue

                q.append(new_pos)

        return False

    # Check every position on board
    for i in range(0, rows):
        for j in range(cols):
            if board[i][j] == 0:
                # run bfs
                visit = set()
                pos = (i, j)
                if not bfs(pos, visit):
                    return False
    return True


print(find_path(board4, end1))
