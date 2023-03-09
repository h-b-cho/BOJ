import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    total = 0
    plus = 0
    inp = input().strip()
    for j in inp:
        if j == "X":
            plus = 0
        else:
            plus += 1
        total += plus

    print(int(total))