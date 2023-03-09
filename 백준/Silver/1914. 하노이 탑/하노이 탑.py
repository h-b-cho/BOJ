import sys
input = sys.stdin.readline
N = int(input())

def iHanoiYou(N):
    K = 2**N-1
    def Hanoi(N, start, to, via):
        if N==1:
            print(start, to)
        else:
            Hanoi(N-1, start, via, to)
            print(start, to)
            Hanoi(N-1, via, to, start)
    print(K)
    if N <= 20:
        Hanoi(N, 1, 3, 2)
iHanoiYou(N)