h, m = map(int, input().split())
t = int(input())

m += t
while m > 59:
    h += 1
    m -= 60
while h > 23:
    h -= 24

print(h, m)