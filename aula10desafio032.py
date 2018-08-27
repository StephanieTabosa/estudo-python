# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano = int(input('Qual o ano você deseja saber se é BISSEXTO? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O número {} é SIM um ano BISSEXTO!'.format(ano))
else:
    print('O número {} NÃO é um ano BISSEXTO!'.format(ano))


# 0 'chama' o ano atual da máquina
# from datetime import date
# if ano == 0
# ano = date.today().year





