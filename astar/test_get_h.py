from astar_algorithm_set import AStar

puzzle = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal = [2, 8, 3, 1, 6, 4, 7, 5, 0]


# puzzle와 goal이 h값을 구했을 때 1이 나와야 한다. 근데 16이 나와요

node = AStar(problem=puzzle, answer=goal)
print(node.h())


