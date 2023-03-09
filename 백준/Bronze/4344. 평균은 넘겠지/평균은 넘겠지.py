import sys
input = sys.stdin.readline

c = int(input())

for i in range(c):
  arr = list(map(int, input().split()))
  scores = arr[1:]
  avrge = sum(scores)/arr[0] 

  p = 0
  for score in scores:
    if score>avrge:
      p += 1
      
  # print( str(round(p/arr[0], 5)*100) + '%' ) # 왜 오답?
  # print(f'{p/arr[0]*100:.3f}%')
  print('{0:.3f}%'.format(p/arr[0]*100))