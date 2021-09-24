budgets = [120, 110, 140, 150]

def solution(budgets, M):
    budgets = sorted(budgets)
    print(sum(budgets), M,sum(budgets) - M)
    if sum(budgets) <= M:
        return budgets[len(budgets)-1]

    print(budgets)
    pass


solution(budgets, 485)