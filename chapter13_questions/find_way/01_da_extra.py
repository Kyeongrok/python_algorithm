def get_another(num):
    if num == 0:
        return 1
    else:
        return 0

def get_paths(graph, start, goal):
    queue = [start]
    result = []

    while queue:
        n, path = queue.pop()
        if n == goal:
            result.append(path)
        else:
            graph[n].pop()

def solution(roads):
    print("-------")
    graph = {}
    for road in roads:
        # graph[road[0]][road[1]] = road[2]
        for graph_idx in range(2):
            if graph.get(road[graph_idx]) == None:
                graph[road[graph_idx]] = {}
            if graph[road[graph_idx]].get(road[get_another(graph_idx)]) == None:
                graph[road[graph_idx]][road[get_another(graph_idx)]] = 0
            graph[road[graph_idx]][road[get_another(graph_idx)]] = road[2]

    print(graph)


road = [[1,2,2],[1,5,1],[2,3,1],[2,4,2],[2,6,3],[3,4,2],[4,5,1]]
solution(road)
