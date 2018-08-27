valorProduto = float(input('Valor do produto R$ '))
avista = valorProduto-(10/100*valorProduto)
aprazo = valorProduto+(15/100*valorProduto)

print('O produto custa R${:.2f}.'.format(valorProduto))
print('Se você comprar à vista, o produto sairá por R${:.2f}.'.format(avista))
print('Se você for parcelar sua compra, seu produto terá um aumento de 15% e custará R${:.2f}.'.format(aprazo))


