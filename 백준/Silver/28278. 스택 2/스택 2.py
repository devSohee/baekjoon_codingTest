import sys
stk = []
for _ in range(int(input())):
    t_ = sys.stdin.readline().rstrip().split()
    match int(t_[0]):
        case 1:
            stk.append(int(t_[1]))
        case 2:
            print(stk.pop() if stk else -1)
        case 3:
            print(len(stk))
        case 4:
            print(0 if stk else 1)
        case 5:
            print(stk[-1] if stk else -1)
