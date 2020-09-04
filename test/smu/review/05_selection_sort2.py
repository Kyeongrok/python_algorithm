list = [8, 2, 9, 67, 9]

def selection_sort(list):
    for i in range(len(list) - 1):

        for j in range(i + 1, len(list)):
            print(i, j)

selection_sort(list)
