# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Ângulo desejado: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo {}º possui SENO: {:.2f}.'.format(angulo,seno))
print('O ângulo {}º possui COSSENO: {:.2f}.'.format(angulo, cosseno))
print('O ângulo {}º possui TANGENTE: {:.2f}.'.format(angulo, tangente))







