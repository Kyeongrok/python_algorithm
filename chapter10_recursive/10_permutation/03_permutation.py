def permutation(alphabets, current_permutation):

    if len(current_permutation) == len(alphabets):
        print(current_permutation)
        return

    for c in alphabets:
        if c not in current_permutation:
            permutation(alphabets, current_permutation + [c])

permutation('ABC', [])