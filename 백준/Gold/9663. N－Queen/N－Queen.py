import sys  
input = sys.stdin.readline
N = int(input())
pos = [0]*N
flag_a = [False]*N
flag_b = [False]*(N*2-1)
flag_c = [False]*(N*2-1)
count = 0

def set(n, end):
    global count
    for j in range(end):
        if ( not flag_a[j]
             and not flag_b[n+j]
             and not flag_c[n-j+end-1] ):
            pos[n] = j
            if n==end-1:
                count+=1
            else:
                flag_a[j] = flag_b[n+j] = flag_c[n-j+end-1] = True
                set(n+1, end)
                flag_a[j] = flag_b[n+j] = flag_c[n-j+end-1] = False
    return count

print(set(0, N))