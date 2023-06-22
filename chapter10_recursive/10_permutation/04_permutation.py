
def generate_permutations(alphabet, current_permutation):
    # 기저 사례: 현재 순열의 길이가 알파벳의 길이와 동일한 경우 출력
    if len(current_permutation) == len(alphabet):
        print(current_permutation)
        return

    # 선택되지 않은 문자들을 반복하여 재귀 호출
    for char in alphabet:
        if char not in current_permutation:
            # 현재 문자를 선택한 순열에 추가하고 재귀 호출
            generate_permutations(alphabet, current_permutation + char)


# 알파벳 문자열
alphabet = 'ABC'

# 순열 생성 함수 호출
generate_permutations(alphabet, "")
