# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Digite o seu salário R$ '))
aumento = salario+(15/100*salario)
print('Seu salário era R$ {:.2f}. Com um aumento de 15%, passou a ser R$ {:.2f} !!!'.format(salario,aumento))


