import sys
read = sys.stdin.readline

x = int(read())

if x%4==0 and x%100!=0 or x%400==0:
  print(1)
else:
  print(0)