import sys
from itertools import permutations
input = sys.stdin.readline
isMax = 0
N = int(input())
lst = list(map(int, input().split()))

for set in list(permutations(lst)):
    setSum = 0
    for i in range(N-1):
        setSum += abs(set[i]-set[i+1])
    if setSum>isMax:
        isMax=setSum
print(isMax)
