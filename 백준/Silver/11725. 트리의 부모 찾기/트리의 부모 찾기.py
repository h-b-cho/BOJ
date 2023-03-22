import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [int(0) for _ in range(N+1)]
q = deque([1])

def bfs():
    while q:
        curr = q.popleft()
        # if parent[curr[0]]==0:
        for curr_adjacent in graph[curr]:
            if parent[curr_adjacent]==0:
                parent[curr_adjacent] = curr
                q.append(curr_adjacent)

bfs()
for x in parent[2:]: print(x)