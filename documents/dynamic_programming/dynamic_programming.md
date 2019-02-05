# Dynamic Programming
https://www.geeksforgeeks.org/top-20-dynamic-programming-interview-questions/

# Overlapping Subproblems
다이내믹 프로그래밍은 복잡한 문제를 여러개의 서브 문제로 나누어서 각 서브 문제의 결과를 저장해서 같은 연산을 반복해서 수행하지 않도록 하는 프로그래밍 기법입니다.
아래 예제는 다이내믹 프로그래밍 기법의 두가지 주요 요소를 적용해서 풀어내기에 좋은 예제 입니다.

이 문제에서는 첫번째 요소인 Overlapping Subproblems를 자세히 살펴볼 예정입니다.
두번째 문제는 다음 글에서 다루겠습니다.

자르고 공략하는(Divide and Conquer) 방법과 같이 다이내믹 프로그래밍은 sub-problems를 풀기 위해 솔루션을 조합해서 사용합니다.
다이내믹 프로그래밍은 같은 sub problems를 반복해서 풀어내야 할 때 사용합니다.
다이내믹 프로그래밍에서는 이미 연산이된 결과들을 다시 연산하지 않도 표에 저장 해놓습니다.
다이내믹 프로그래밍은 반복되는 하위 문제가 없을때는 유용하지가 않습니다. 왜냐하면 중간 연산결과를 저장할 필요가 없기 때문입니다.
바이너리 서치(이진 탐색)는 하위 문제가 없기 때문에 다이내믹 프로그래밍 기법이 필요 없습니다.
하지만 피보나치 수열 문제를 풀어야 하는 경우는 하위 문제가 반복되어 나옵니다.

fib(3)연산은 두번 반복이 됩니다. 이 결과를 저장 해놓는다면 연산을 여러번 할 필요 없이 저장 해놓은 값을 불러오기만 하면 됩니다.
연산 결과를 저장하는데는 두가지 방법이 있습니다. 메모이제이션(Memoization), 타뷸레이션(Tabulation)입니다.
메모이제이션은 Top Down방식이고 타뷸레이션은 Bottom Up방식입니다.


# Optimal Substructure
아래 주어진 문제는 최적의 서브 구조의 요소를 가지고 있다.

Shortest Path 알고리즘은 Optimal Substructure를 가지고 있지만
Longest Path는 최적 서브구조를 가지고 있지 않다.

 


# Longest Common Subsequence

# Longest Increasing Subsequence
# Edit Distance