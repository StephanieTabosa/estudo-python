# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex.: Digite um número: 1834.
# Unidade: 4; dezena: 3; centena:8; milhar:1.
#unidade = numero[3]
#dezena = numero[2]
#centena = numero[1]
#milhar = numero[0]

numero = int(input('Digite um número inteiro entre 0 e 9999: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'ciano': '\033[36m',
         'lilas': '\033[35m'
         }

print('O número {} possui: '.format(numero))
print('Milhar {}{}{}'.format(cores['lilas'], m, cores['limpa']))
print('Centena {}{}{}'.format(cores['ciano'], c, cores['limpa']))
print('Dezena {}{}{}'.format(cores['amarelo'], d, cores['limpa']))
print('Unidade {}{}{}'.format(cores['vermelho'], u, cores['limpa']))
















