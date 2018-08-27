# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print('-=-'*10)
print('Analisando um triângulo')
print('-=-'*10)
A = float(input('Qual o tamanho da primeira reta? '))
B = float(input('Qual o tamanho da segunda reta? '))
C = float(input('Qual o tamanho da terceira reta? '))

if (B - C) < A < B + C and (A - C) < B < A + C and (A - B) < C < A + B:
    print('É possível criar um triângulo com os valores fornecidos!')
else:
    print('Não será possível a criação de um triângulo!')

