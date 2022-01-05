lar = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede:'))
di = lar*alt
print('A área da sua parede é:{:.2f}m²,'.format(di))
print('E você vai precisar de {:.2f} litros de tinta para pintala '.format(di/2))
