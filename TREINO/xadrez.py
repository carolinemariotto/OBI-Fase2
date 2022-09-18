
[N, T] = [int(i) for i in input().split() ]
res = 0 

if T == 0 :
    res = N 
    
elif T == 1:
    res = N *(N-1)