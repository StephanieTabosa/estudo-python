# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
numero = random.randint(0, 5)
print('\n***JOGO DA ADIVINHAÇÃO DOS NÚMEROS***')
adivinhar = int(input('Digite um número entre 0 e 5 que você acha que foi o sorteado: '))
print('PROCESSANDO...')
time.sleep(2)
if adivinhar == numero:
    print('Que legal!!! Você acertou e venceu o jogo!')
else:
    print('Puxa, que pena! Você perdeu, pensei no número {} e não no número {}... Tente outra vez!'.format(numero, adivinhar))











