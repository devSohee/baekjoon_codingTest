def solution(x):
    n = x
    s = 0
    while n:
        s += n % 10
        n //= 10
    print(s, x)
    print(n % s)
    if x % s:
        return False
    return True