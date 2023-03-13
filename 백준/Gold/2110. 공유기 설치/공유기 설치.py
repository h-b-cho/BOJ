import sys
input = sys.stdin.readline
N, C = input().split()
N = int(N)
C = int(C)
places = sorted(list(int(input()) for _ in range(N)))
placerange = places[1:]

result = 0

def binary_search(start, end):
    global result
    while start <= end:
        mid = (start+end) // 2
        cnt = 1
        cur = places[0]
        for i in placerange:
            if i - cur >= mid:
                cnt += 1
                cur = i
        if cnt >= C:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

print(binary_search(1, places[-1]-places[0])) # == (1, max(places)-min(places))