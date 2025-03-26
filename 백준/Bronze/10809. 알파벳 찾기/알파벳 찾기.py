a=[-1]*26
s=input()
for i in s:
    t=ord(i)-97
    if a[t] == -1:a[t]=s.index(i)
print(*a)