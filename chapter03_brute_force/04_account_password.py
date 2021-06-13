def solution(pw):
    # h i j k
    for h in range(0, 10):
        for i in range(0, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    print(f'{h}{i}{j}{k}')
solution(3427)