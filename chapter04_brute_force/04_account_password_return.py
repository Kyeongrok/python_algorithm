def solution(pw):
    # h i j k
    for h in range(0, 10):
        for i in range(0, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    made_pw = f'{h}{i}{j}{k}'
                    if str(pw) == made_pw: # 만들어진 pw와 입력받은 pw비교
                        print(made_pw)
                        return True
print(solution(3427))