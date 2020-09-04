def and_gate(x1, x2):
    # x1, x2를 넣었을 때 둘다 1이어야만 1이 출력되는 gate
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1

print(and_gate(0, 0))
print(and_gate(1, 0))
print(and_gate(0, 1))
print(and_gate(1, 1))

