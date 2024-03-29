import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
shots = list(map(int, input().split()))
animals = []
for i in range(N):
    a, b = map(int, input().split())
    animals.append((a, b))

cnt = 0
shots.sort()

for a, b in animals:
    start, end = 0, len(shots)-1
    mid = 0
    while start < end:
        mid = (start+end)//2

        if shots[mid] < a:
            start = mid+1
        else:
            end = mid

    if abs(shots[end]-a)+b<=L:
        cnt += 1

print(cnt)