def solution(n):
    answer = 0
    for i in range(1, n + 1):
        yak = 0
        for y in range(1, i + 1):
            if i % y == 0:
                yak += 1
        if yak > 2:
            answer += 1
    return answer