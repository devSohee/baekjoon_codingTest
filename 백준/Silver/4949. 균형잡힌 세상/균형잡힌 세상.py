while 1:
    stk_s = []
    stk_b = []
    priority = []
    isVPS = True
    s = input()
    if s == '.':
        break
    for ch in s:
        if ch == '(':
            priority.append(1)
            stk_s.append(ch)
        elif ch == ')':
            if stk_s and priority[-1] == 1:
                stk_s.pop()
                priority.pop()
            else:
                isVPS = False
                break
        elif ch == '[':
            priority.append(2)
            stk_b.append(ch)
        elif ch == ']':
            if stk_b and priority[-1] == 2:
                stk_b.pop()
                priority.pop()
            else:
                isVPS = False
                break
    if len(stk_s) or len(stk_b):
        isVPS = False
    print('yes' if isVPS else 'no')