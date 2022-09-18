P1 = int(input())
P2 = int(input())
P3 = int(input())
P4 = int(input())
P5 = int(input())
trofeu = 0
placas = 0
lista = [P1,P2,P3,P4,P5]
lista.sort(reverse=True)

maior = lista[0]

def contarMaior(listatotal,maior):
  count = 0
  for item in listatotal:
    if(item == maior):
      count += 1
  return(count)

trofeu = contarMaior(lista,maior)

if trofeu < len(lista):
  segundomaior = lista[trofeu]
  placa = contarMaior(lista,segundomaior)
else:
  placa = 0

print(trofeu,placa)