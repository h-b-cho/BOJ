import sys 
input = sys.stdin.readline
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

# print((int(A)**int(B))%int(C)) # 시간초과-_-

def dac(a, b, c):
  if b==1:
      return a%c
  else:
      tmp = dac(a, b//2, c)
      if b%2==0:
          return (tmp * tmp) % c
      else:
          return (tmp * tmp * a) % c

print(dac(A, B, C))