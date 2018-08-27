# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0.15 por KM rodado.

kmpercorrido = float(input('Digite a quilometragem percorrida: '))
diasalugados = int(input('Digite a quantidade de dias que o carro foi alugado: '))
diaria = diasalugados*60
valorporkm = kmpercorrido*0.15

print('O carro foi alugado por {} dias e percorreu {} Km.'.format(diasalugados, kmpercorrido))
print('O valor das diárias custaram R$ {:.2f}.'.format(diaria))
print('O valor do quilometro rodado totalizou em R$ {:.2f}.'.format(valorporkm))
print('Sendo assim, o valor total a ser pago será R$ {:.2f}.'.format(diaria+valorporkm))


#ou total = (diasalugados*60)+(kmpercorrido*0.15)
# print ('O valor total a ser pago será R$ {}.'.format(total))











