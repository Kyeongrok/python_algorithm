from astar.astar_algorithm import expand_child, AStar

puzzle = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
node = AStar(problem=puzzle, answer=goal)
r = expand_child(node)


# for item in r:
#     print(item.problem)
