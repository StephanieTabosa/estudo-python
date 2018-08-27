# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Digite a largura (em metros) desejada: '))
altura = float(input('Digite a altura (em metros) desejada: '))
area = largura*altura
tintaNecessaria = area/2

print('Você vai precisar de {} litros de tinta para pintar uma área de {} m²!'.format(tintaNecessaria,area))


