graph = {"A":["B", "C"]}
graph["B"] = ["A", "D"]
graph["C"] = ["A"]
graph["D"] = ["B"]
print(graph["A"])
print(graph["B"])
print(graph["C"])
print(graph["D"])
