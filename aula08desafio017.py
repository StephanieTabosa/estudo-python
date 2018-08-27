#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa

import math
cOpos = float(input('Digite um número para ser cateto oposto: '))
cAdj = float(input('Digite um número para ser cateto adjacente: '))
hipotenusa = math.hypot(cAdj, cOpos)
print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))












