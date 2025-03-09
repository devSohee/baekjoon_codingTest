stk = []
for _ in range(int(input())):
    k = int(input())
    if k:
        stk.append(k)
    else:
        stk.pop()
print(sum(stk))