list = [3, 8, 9, 5, 4, 2]
odds = []
evens = []

for item in list:
    if(item % 2 == 1):
        odds.append(item)
    else:
        evens.append(item)

print("odds:", odds)
print("evens:", evens)

