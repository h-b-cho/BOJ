import sys
from itertools import combinations
input = sys.stdin.readline

arr = []
for _ in range(9):
  arr.append(int(input()))

for i in combinations(arr, 7): # 7명의 키 == 100인 경우를 찾는다.
	if sum(i)==100:
		ans = sorted(i)
for ans_ in ans:
	print(ans_)