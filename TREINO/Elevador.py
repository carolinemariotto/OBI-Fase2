[Numero] = [int(i) for i in input().split()]
[peso] = [int(i) for i in input().split()]

peso.sort()
peso[0:0] = [0]


for i in range(Numero):
    if( peso[i+1] - peso[i] > 8):
        res = 'N'
        break
    else:
        res = 'S'
    
print(res)