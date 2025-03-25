def solution(babbling):
    answer = 0
    bbl = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for bb in bbl:
            if bb in b:
                b = b.replace(bb, ' ')
            print(b)
        if b.count(' ') == len(b): 
            answer += 1
    return answer