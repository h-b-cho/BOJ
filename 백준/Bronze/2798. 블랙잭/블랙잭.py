import sys
from itertools import combinations
input = sys.stdin.readline

# N장의 카드에 써져 있는 숫자가 주어졌을 때, sum<M, sum이 최대이 경우의 카드 3장 조합을 구해 출력하시오.

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
largest_sum = 0

for card_comb in combinations(card_list, 3):
	temp_sum = sum(card_comb)
	if temp_sum>largest_sum and temp_sum<=M:
		largest_sum=temp_sum

print(largest_sum)