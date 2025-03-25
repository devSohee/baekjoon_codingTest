def solution(mats, park):
    mats.sort(reverse = True)
    for m in mats:
        for i in range(0, len(park) - mats[-1] + 1):
            for j in range(0, len(park[0]) - mats[-1] + 1):
                if park[i][j] == '-1':
                    if min(len(park[i:]), len(park[i][j:])) < m:
                        continue
                    else:
                        if mats_check(park, i, j, m):
                            return m
    return -1

def mats_check(park, r, c, mats):
    p = mats ** 2
    for i in range(r, r + mats):
        for j in range(c, c + mats):
            if park[i][j] == '-1':
                continue
            else: 
                return False
    return True