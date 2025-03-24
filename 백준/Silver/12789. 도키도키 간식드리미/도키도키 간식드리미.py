order = 1
N = int(input())
stk = []
for i in map(int, input().split()):
    if i == order:
        order += 1
        while stk:
            if stk[-1] == order:
                order += 1
                stk.pop()
            else:
                break
    else:
        stk.append(i)

print("Sad" if stk else "Nice")