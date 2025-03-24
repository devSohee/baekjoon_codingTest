def solution(k, m, score):
    answer = 0
    score.sort()
    for i in range(len(score)//m):
        answer += min(score[-m * (i + 1): len(score)-(i * m)]) * m
    return answer