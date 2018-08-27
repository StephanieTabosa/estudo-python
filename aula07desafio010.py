# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ = R$ 3,27
dinheiro = float(input('Digite quanto você tem de dinheiro na carteira. R$'))
conversao = dinheiro/3.27

print('Você possui R$ {:.2f} e pode comprar US$ {:.2f}.'.format(dinheiro,conversao))









