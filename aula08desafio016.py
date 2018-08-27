# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX.: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

import math
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, math.trunc(num)))

#ou print('O número {} tem a parte inteira {}.'.format(num, int(num))) SEM O 'IMPORT MATH'



