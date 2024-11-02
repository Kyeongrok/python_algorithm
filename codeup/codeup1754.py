
n1 = "9997"
n2 = "9998"
'''
'''

received_str = input().split(' ')
#received_str = '111111111111111111111111111121 111111111111111111111111111112'.split(' ')
n1 = received_str[0]
n2 = received_str[1]

printed = False
if len(n1) < len(n2):
    print(n1, n2)
    printed = True
elif len(n1) == len(n2):
    for i in range(len(n1)):
        if n1[i] < n2[i]:
            print(n1, n2)
            printed = True
            break
        else:
            print(n2, n1)
            printed = True
            break

if not printed:
    print(n2, n1)


