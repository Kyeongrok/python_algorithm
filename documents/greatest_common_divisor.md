# 최대공약수(Greatest Common Divisor)
gcd라고 많이 쓴다. gcm이라고도 쓴다.

## 핵심로직
큰쪽에서 작은쪽을 뺀다.
* gcd(196, 42) = gcd(196 - 42, 42)
