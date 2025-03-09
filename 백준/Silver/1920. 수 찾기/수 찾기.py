import sys

input = sys.stdin.readline

int(input())
N = input().rstrip().split()
N = set(N)
M = int(input())
M_ = input().rstrip().split()

for _ in range(M):
    print(1 if M_[_] in N else 0)
