def solution(k, score):
    answer = []
    honor = []
    for i in range(len(score)):
        if i < k:
            honor.append(score[i])
            answer.append(min(honor))
            print(i, honor, 3)
        else:
            if min(honor) < score[i]:
                honor.remove(min(honor))
                honor.append(score[i])
                answer.append(min(honor))
                print(i, honor, -1)
            else:
                answer.append(min(honor))
            
    return answer