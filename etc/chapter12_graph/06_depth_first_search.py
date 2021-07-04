
graph = {
    "A":["B", "C"],
    "B":["A", "D"],
    "C":["A"],
    "D":["B"]
}
stack = ["D"]
visited = []

while stack:
    current = stack.pop()
    visited.append(current)
    for item in graph[current]:
        if item not in visited:
            stack.append(item)
    print(visited)
