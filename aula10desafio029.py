# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade que o carro estava: '))
excedente = velocidade-80
valorMulta = excedente*7
if velocidade > 80:
    print('Você foi multado(a) por estar a {:.1f}Km/h. Limite 80Km/h'.format(velocidade))
    print('Será gerada uma multa no valor de R$ {:.2f}.'.format(valorMulta))
else:
    print('Tenha uma ótima semana. Dirija com segurança!')

















