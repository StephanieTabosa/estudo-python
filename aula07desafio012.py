# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

valorInicial = float(input('Digite o preço do produto sem o desconto em R$ '))
valorDesconto = valorInicial-(5/100*valorInicial)
print('O seu produto custa R$ {:.2f}, mas com desconto de 5% agora custa R$ {:.2f}!!!'.format(valorInicial,valorDesconto))

