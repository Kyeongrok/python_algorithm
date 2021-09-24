def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                print("-------")
                return False
    return answer


print(solution(['119', '97674223', '1195524421']))
print(solution(["12","123","1235","567","88"]))
print(solution(['123','456','789']))
