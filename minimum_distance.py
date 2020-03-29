"""
Given a 2D grid of 0s, 1s, and a single 2, with the start position the top-left
corner, determine the minimum distance need to travel to the 2.

0s represent traversable land.
1s represent "water" that we cannot traverse.
2 represents our final goal.

The top-left corner will always be a 0. We will try to reach the 2 by
traversing through land. We are only allowed to traverse up/left/down/right,
with no diagonal movement allowed. If the 2 cannot be reached, return -1.

Examples:

Input:
[
  [0, 0, 1, 1],
  [2, 0, 1, 0],
  [1, 0, 0, 0]
]
Output: 1 (starting at the top-left corner, move down)

Input:
[
  [0, 0, 1, 1],
  [0, 0, 1, 2],
  [1, 0, 0, 0]
]
Output: 6 (starting at the top-left corner, either move
down-right-down-right-right-up, or right-down-down-right-right-up)

Input:
[
  [0, 0, 0, 1, 1, 0, 2, 0]
]
Output: -1 (the 2 is not reachable by land)

Hint:

Apply the general principles of breadth-first search. Maintain a queue of
positions with their distances. When consuming each position, check to see which
neighbors are traversable and haven't already been visited.
"""

def minimum_distance(grid): 
    if len(grid) == 0:
        return -1
    
    # store (row, col, steps_taken) in queue
    # check if (row+1, col) or (row, col+1) is out of index. if not, check if equal to 0, if so, push to queue.
    # if grid[row][col] is 2, end 
    # how to check if already visited? use a "visited" list
    
    path = [[0,0,0]]
    visited = []
    
    while len(path) > 0:
        temp = path.pop(0)
        row = temp[0]
        col = temp[1]
        visited.append([row, col])
        distance = temp[2]

        if grid[row][col] == 2:
            return distance
        
        # check movement to down
        if 0 <= (row + 1) < len(grid):
            if (grid[row + 1][col] != 1) & ([row + 1, col] not in visited):
                path.append([row + 1, col, distance + 1])
        # check movement to up
        if 0 <= (row - 1) < len(grid):
            if (grid[row - 1][col] != 1) & ([row - 1, col] not in visited):
                path.append([row - 1, col, distance + 1])     
        # check movement right
        if 0 <= (col + 1) < len(grid[0]):
            if (grid[row][col + 1] != 1) & ([row, col + 1] not in visited):
                path.append([row, col + 1, distance + 1])
        # check movement left
        if 0 <= (col - 1) < len(grid[0]):
            if (grid[row][col - 1] != 1) & ([row, col - 1] not in visited):
                path.append([row, col - 1, distance + 1])
        
    return -1