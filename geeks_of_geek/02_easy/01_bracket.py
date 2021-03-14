brackets = "[{()}]" # true
brackets2 = "[{(}]" # false
brackets3 = "[{(}])" # false

stack_a = []
stack_b = []

for letter in brackets:
    stack_a.append(letter)

stack_a.pop()

for idx in range(0, 10):
    print(idx)