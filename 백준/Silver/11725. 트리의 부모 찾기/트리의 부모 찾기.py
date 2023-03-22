import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [int(0) for _ in range(N+1)]

def dfs(n):
    for i in graph[n]:
        if parent[i]==int(0):
            parent[i] = n
            dfs(i)

dfs(1)
for j in range(2, N+1): print(parent[j])