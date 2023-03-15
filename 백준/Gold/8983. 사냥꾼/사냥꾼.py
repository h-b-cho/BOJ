import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
shots_p = list(map(int, input().split()))
animals_p = []
for i in range(N):
    a, b = map(int, input().split())
    animals_p.append((a, b))

answer = 0
shots_p.sort()

# print(M, N, L)
# print(shots_p)
# print(animals_p)

for a, b in animals_p:
    start, end = 0, len(shots_p)-1
    mid = 0
    while start < end:
        mid = (start+end)//2

        if shots_p[mid] < a:
            start = mid+1
        elif shots_p[mid] > a:
            end = mid-1
        else:
            start = mid
            break

    # L <= abs(a-x)+b에 해당하는 동물이 각 사대에서 잡을 수 있는 동물.

    # 동물의 위치를 하나씩 탐색하며 
    # a+(b-L) <= x <= a-(b-L)에 해당하는 위치에 사대가 있다면, 
    # 해당 동물은 사냥 가능한 것으로 판단한 뒤 카운트해준다. 
    # 단, L > b 인 경우만 해당한다.

    if abs(shots_p[start]-a)+b <= L:
        answer += 1
    elif start+1 < len(shots_p) and abs(shots_p[start+1]-a)+b <= L:
        answer += 1
    elif start > 0 and abs(shots_p[start-1]-a)+b <= L:
        answer += 1

print(answer)