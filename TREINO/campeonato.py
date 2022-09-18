N = [ int(i) for i in input().split()]

for i in range(N):
    if N[i] == 1:
        a = i+1
    elif N[i] == 9:
        b = i+1
        
if a < b :
    a,b = b,a
    
if a <= 8 and b > 8 :
    print('final')
    
elif a <= 4 and b > 4 :
    print('semifinais')
    
elif (a % 2 == 1) and (b == a + 1):
    print('oitavas')
else:
    print('quartas')