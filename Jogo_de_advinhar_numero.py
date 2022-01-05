import random
print('=================')
print('ADIVINHE O NÚMERO')
print('=================')
vj = input('Vamos jogar? Digite sim ou não').upper().strip()
if 'SIM' == vj:
    print('Que maravilha, vamos continuar!')
else:
    print('Que pena, até logo.')
    exit()
lista = [1, 2, 3, 4, 5]
mis = random.choice(lista)
pc = int(input('Estou pensando em um número entre 0 e 5. Qual você acha que é?'))
if pc == mis:
    print('PARABÉNS você acertou!')
else:
    print('VOCÊ ERROU! Eu estava pensando no {}.'.format(mis))
