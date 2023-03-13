import sys
input = sys.stdin.readline
N = int(input())
litters = sorted(list(map(int, input().split())))

def binary_search(arr:list):
    min   = 0
    max   = N-1
    sum   = abs(arr[min]+arr[max])
    result = [arr[min], arr[max]]

    while min<max:
        arrMin = arr[min]
        arrMax = arr[max]

        tmpsum = arrMin+arrMax

        if abs(tmpsum)<sum:
            sum = abs(tmpsum)
            result = [arrMin, arrMax]
            if sum==0:
                break

        if tmpsum<0:
            min+=1
        else: 
            max-=1

    print(result[0], result[1])

binary_search(litters)