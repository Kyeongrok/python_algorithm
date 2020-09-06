import re

def luhn(card_number):
    card_number = card_number.replace('-', '')
    middle_sum = 0
    for i in range(0, len(card_number)-1, 2):
        multiple2 = int(card_number[i]) * 2
        if multiple2 >= 10:
            middle_sum += multiple2 // 10 + multiple2 % 10
        else:
            middle_sum += multiple2
        middle_sum += int(card_number[i+1])

    # print(middle_sum % 10)
    return middle_sum % 10 == 0


def validation(card_no):
    if len(card_no) > 20 and len(card_no) < 1:
        return False
    match_obj = re.search('([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}|[0-9]{16})', card_no)
    print(match_obj)
    return match_obj != None


def solution(card_numbers):
    answer = []
    for i in range(len(card_numbers)):
        if validation(card_numbers[i]) == False:
            answer.append(0)
        elif luhn(card_numbers[i]):
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution(["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245",
                "3285376499342459", "3285-3764-9934-2452", "1234567890123456", '3444063910462763']))

