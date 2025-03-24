def solution(s):
    stk = []
    for ch in s:
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                return False

    if len(stk) > 0:
        return False
    return True