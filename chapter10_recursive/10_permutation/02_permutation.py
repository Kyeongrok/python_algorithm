def permutation(current_permutation):
    alphabets = 'ABC'

    if len(current_permutation) == 3:
        print(current_permutation)
        return

    # 선택되지 않은 문자들을 반복하여 재귀 호출
    for c in alphabets:
        if c not in current_permutation:
            # 현재 문자를 선택한 순열에 추가하고 재귀 호출
            permutation(current_permutation + [c])

permutation([])