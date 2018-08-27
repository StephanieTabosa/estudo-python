# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200km,
# e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distância, em Km, da viagem? '))
if distancia <= 200:
    print('O valor da passagem será R$ {:.2f}'.format(distancia*0.50))
else:
    print('O valor da passagem será R$ {:.2f}'.format(distancia*0.45))
