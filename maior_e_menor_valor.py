vl1 = int(input('Digite o primeiro valor: '))
vl2 = int(input('Digite o segundo valor: '))
vl3 = int(input('Digite o terceiro valor: '))
if vl1 > vl2 and vl1 > vl3:
    maior = vl1
if vl2 > vl3 and vl2 > vl1:
    maior = vl2
if vl3 > vl2 and vl3 > vl1:
    maior = vl3
if vl1 < vl2 and vl1 < vl3:
    menor = vl1
if vl2 < vl3 and vl2 < vl1:
    menor = vl2
if vl3 < vl2 and vl3 < vl1:
    menor = vl3
print('O menor número é {} '.format(menor))
print('O maior número é {} '.format(maior))
