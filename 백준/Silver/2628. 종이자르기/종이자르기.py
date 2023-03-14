W, H = list(map(int, input().split()))
row = [0, W]
column = [0, H]
N = int(input())
num = 0
lst = []
for _ in range(N):
  a, b = map(int, input().split())
  if a==0:
    column.append(b)
  else:
    row.append(b)
row.sort()
column.sort()

def maxfinder(row, column):
  for i in range(0, len(row)-1):
    for j in range(0, len(column)-1):
      num = (row[i+1]-row[i]) * (column[j+1]-column[j])
      lst.append(num)
  print(max(lst))
maxfinder(row, column)