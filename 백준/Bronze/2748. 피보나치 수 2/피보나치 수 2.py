import sys
input = sys.stdin.readline
N = int(input())

f = [0, 1]

for n in range(1, N):
    f.append(f[n]+f[n-1])

print(f[-1])