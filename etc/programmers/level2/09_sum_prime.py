# sieve
# how to make prime
# n C 3
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    answer += 1
    return answer

print(solution([1, 2, 4]) == 1)
print(solution([1, 2, 7, 6, 4]) == 4)
