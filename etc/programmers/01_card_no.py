import re
# 통과한 test
'''
validation이 까다로운 문제였음.
특히 try except안걸면 런타임 에러나는 구간이 있음.
'''
def luhn(card_number):
    card_number = card_number.replace('-', '')
    middle_sum = 0
    odd_sum = 0
    for i in range(0, len(card_number)-1, 2):
        multiple2 = int(card_number[i]) * 2
        if multiple2 >= 10:
            middle_sum += multiple2 // 10 + multiple2 % 10
        else:
            middle_sum += multiple2
        odd_sum += int(card_number[i+1])
    # print(middle_sum, odd_sum)
    return (middle_sum + odd_sum) % 10 == 0


def validation(card_no):
    if len(card_no) > 20 and len(card_no) < 1:
        return False
    # -가 3개인 경우
    if '-' in card_no:
        if card_no[4] != '-' or card_no[9] != '-' or card_no[14] != '-':
            return False

    # 숫자, -말고 다른 것도 있는지
    replaced = re.sub("([0-9]|\-)", "", card_no)
    if replaced != '':
        return False

    # 16자리가 아닌 경우
    card_number = card_no.replace('-', '')
    if len(card_number) != 16:
        return False
    match_obj = re.search('([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}|[0-9]{16})', card_no)
    # print(match_obj)
    return match_obj != None


def solution(card_numbers):
    answer = []
    for i in range(len(card_numbers)):
        try:
            if validation(card_numbers[i]) == False:
                answer.append(0)
            elif luhn(card_numbers[i]):
                answer.append(1)
            else:
                answer.append(0)
        except Exception as e:
            answer.append(0)

    return answer

print(solution(["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245",
                "3285376499342459", "3285-3764-9934-2452", "1234567890123456", '3444063910462763',
                '344406391046276', "32853-764-9934-2453","3285-3764-9934-2+53", '',
                '000000000000'
                ]))

# print(luhn("3285-3764-9934-2453"))
replaced = re.sub("([0-9]|\-)", "", '0123456789-+')
print(replaced)