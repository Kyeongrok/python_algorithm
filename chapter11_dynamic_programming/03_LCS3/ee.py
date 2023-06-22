def lcs(X , Y):
    # 주어진 문자열의 길이를 구함.
    m = len(X)
    n = len(Y)

    # DP 값을 저장하기 위한 배열을 선언
    L = [[None]*(n+1) for i in range(m+1)]

    """L[m+1][n+1] 를 bottom up 방식으로 채워나갑니다.
    참고: L[i][j] 은  X[0..i-1] 와 Y[0..j-1] 의 LCS 길이를 가지고 있습니다."""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    # L[m][n] 은 X[0..n-1] & Y[0..m-1] 의 LCS 의 길이가 저장되어 있습니다.
    return L[m][n]
#LCS 함수의 마지막

# 위의 알고리즘을 테스트 하기 위한 드라이버 프로그램
X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X, Y))