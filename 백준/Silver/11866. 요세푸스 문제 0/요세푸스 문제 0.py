from collections import deque
import sys  
input = sys.stdin.readline
N, K = input().split()
N = int(N)
K = int(K)
_i = 1
result = []

circle = deque([])
for i in range(1, N+1):
    circle.append(i)

while circle:
    for i in range(0, K-1):
        popl = circle.popleft()
        circle.append( str(popl) )
    result.append( str(circle.popleft()) )
    
answer = ", ".join(result)
print("<"+answer+">")