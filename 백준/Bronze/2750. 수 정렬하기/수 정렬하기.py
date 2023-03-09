import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arrsorted = sorted(arr)
for arritem in arrsorted:
    print(arritem)