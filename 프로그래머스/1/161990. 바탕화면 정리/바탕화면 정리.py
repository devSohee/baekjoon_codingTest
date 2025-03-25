def solution(wallpaper):    
    answer = [len(wallpaper), len(wallpaper[0]), 0, 0]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                answer[0] = answer[0] if answer[0] < i else i
                answer[1] = answer[1] if answer[1] < j else j
                answer[2] = answer[2] if answer[2] > i else i + 1
                answer[3] = answer[3] if answer[3] > j else j + 1
    return answer