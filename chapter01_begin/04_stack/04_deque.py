from collections import deque

stack = deque()
print("type:", type(stack))
stack.append(1)
print(stack)
stack.append(2)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

print(not stack)