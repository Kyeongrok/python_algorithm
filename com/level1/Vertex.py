class Vertex():
    def __init__(self, value, next):
        self.value = value
        self.next = next

vertex1 = Vertex(85)

head = vertex1

print(head.value)
