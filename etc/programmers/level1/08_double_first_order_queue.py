def solution(operations):
    queue = []
    for operation in operations:
        spl = operation.split(" ")
        number = int(spl[1])
        if spl[0] == "I":
            queue.append(number)
        elif spl[0] == "D" and number == 1:
            # 최대값 지움
            queue.index(int(spl[1]))
        elif spl[0] == "D" and number == -1:
            #최소값 지움
            print("---")

        print(spl)
    return []


operations = ["I 7","I 5","I -5","D -1"]
solution(operations)