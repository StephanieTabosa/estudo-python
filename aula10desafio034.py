# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%
# Para salários inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o valor do seu salário? R$ '))
if salario > 1250:
    print('De acordo com o seu salário atual de R$ {:.2f}, você terá um aumento de 10% e passará a receber R$ {:.2f}.'.format(salario, salario+(salario*10/100)))
else:
    print('De acordo com o seu salário atual de R$ {:.2f}, você terá um aumento de 15% e passará a receber R$ {:.2f}.'.format(salario, salario+(salario*15/100)))

#salario = float(input('Qual o valor do seu salário? R$ '))
#if salario <= 1250:
#   novo = salario + (salario * 15/100)
#else:
#   novo = salario + (salario * 10/100)
# print('Quem ganhava R$ {:.2f} passa a ganhar R${:.2f}.'.format(salario, novo))

