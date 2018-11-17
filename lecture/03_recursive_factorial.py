# factorial을 짜보세요 10!의 결과가 나오는
# loop를 쓰지 말고
# 3! 3 * 2 * 1
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)
print(factorial(4))

# 4 * 4 - 1 * 3 -1 * 2 -1