#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from collections import deque

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def isValid(grid, visited, row, col):
    return (row >= 0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0])) \
           and grid[row][col] == 1 and not visited[row][col]

def findShortestPathLength(grid, src, dest):
    i, j = src
    x, y = dest

    if not grid or len(grid) == 0 or grid[i][j] == 0 or grid[x][y] == 0:
        return -1

    (M, N) = (len(grid), len(grid[0]))
    visited = [[False for x in range(N)] for y in range(M)]
 
    q = deque()
    visited[i][j] = True
    q.append((i, j, 0))

    min_dist = sys.maxsize

    while q:
        (i, j, dist) = q.popleft()
        if i == x and j == y:
            min_dist = dist
            break

        for k in range(4):
            if isValid(grid, visited, i + row[k], j + col[k]):
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1))
 
    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1
 
 
if __name__ == '__main__':
    grid = [
        [1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
 
    src = (0, 0)
    dest = (5, 4)
 
    min_dist = findShortestPathLength(grid, src, dest)
 
    if min_dist != -1:
        print(min_dist)
    else:
        print("Путь не может быть найден.")