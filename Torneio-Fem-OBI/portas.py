N, K  = [ int(i) for i in input().split()]

numeroPortas = N+K

def numeroPortas (* num):
    cont = numeroPortas = 0

def contador (l, r, x):
    for l in range(N, K):
        if l < r :
            cont = N + K 
            while cont <= r :
                cont += x
            print (cont)
        
    else:
        cont = l
        while cont >= r:
            cont -= x
            print (cont )