import sys
from itertools import combinations
input = sys.stdin.readline

def lotto(arr):
	temp = []
	temp = list(combinations(arr, 6))
	for i in temp:
		print(' '.join(map(str, i)))
	print()

while True:
	line = list(map(int, input().split()))
	if line[0]==0:
		break
	k = line[0]
	S = line[1:]
	lotto(S)