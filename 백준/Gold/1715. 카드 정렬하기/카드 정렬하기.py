import sys
import heapq
input = sys.stdin.readline
N = int(input())
cards = list(int(input()) for _ in range(N))
h1 = []
h2 = []
tmph = []
tmp0 = 0
tot = 0 
for c in cards:
    if len(h1)==len(h2):
        heapq.heappush(h1, c)
    else:
        heapq.heappush(h2, c)
    if h1 and h2 and h2[0]>h1[0]:
        tar_1_to_2_value = heapq.heappop(h2)
        tar_2_to_1_value = heapq.heappop(h1)
        heapq.heappush(h2, tar_2_to_1_value)
        heapq.heappush(h1, tar_1_to_2_value)
# 언제나 len(h1)>=len(h2)이 된다.

for i in range(len(h1)): heapq.heappush(tmph, h1[i])
for i in range(len(h2)): heapq.heappush(tmph, h2[i])
# 힙 tmph은 힙 h1과 힙 h2을 합친 힙이다.

while len(tmph)>1:
    if N==1:
        tot = 0
        break
    try:
        if int(len(h1)+len(h2))==N:
            tmp1 = heapq.heappop(h1)
            tmp2 = heapq.heappop(h2)
            tot += tmp1+tmp2
            heapq.heappop(tmph)
            heapq.heappop(tmph)
            heapq.heappush(tmph, tmp1+tmp2)
        tmp1 = heapq.heappop(tmph)
        tmp2 = heapq.heappop(tmph)
        tmp0 = tmp1+tmp2
        heapq.heappush(tmph, tmp0)
        tot += tmp0
    except:
        if tmph==[]:
            tot += tmp0+tmp1
            break
print(tot)