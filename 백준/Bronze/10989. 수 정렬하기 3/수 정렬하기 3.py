import sys
input = sys.stdin.readline
n = int(input())
arr = [0]*10000

for _ in range(n):
  inpval = int(input())
  arr[inpval-1]+=1

for i in range(0, 10000):
  # i == inpval-1
  if arr[i]!=0:
    for _ in range(arr[i]):
      print(i+1) # i+1 == inpval