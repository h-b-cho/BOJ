import sys
input = sys.stdin.readline
N = int(input())
_lst = []
for _ in range(N):
  _lst.append(str(input().strip()))

lst = list(set(_lst)) # 자료형 set의 특성을 이용해 중복되는 문자열 삭제

lst_with_len = []
for item in lst:
  lst_with_len.append( [len(item), item] ) # [문자열길이, 문자열] 을 하나의 요소로 가지는 list lst_with_len

lst_by_len = sorted(lst_with_len) # 문자열길이대로 sorted()

for k, v in lst_by_len:
  print(v) # lst_with_len의 두번째 요소인 문자열만 골라 print()