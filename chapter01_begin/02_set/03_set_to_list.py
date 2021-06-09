l1 = [1, 2, 3, 3, 4, 4] # 3도 2개 4도 2개
s1 = set(l1) # list를 set으로 변경
l2 = list(s1) # 중복 제거된 set을 다시 list로
print(l2)