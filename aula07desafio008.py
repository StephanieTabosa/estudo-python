# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = float(input('Digite um valor em metros: '))
centimetros = metros*100
milimetros = metros*1000
dm = metros*10
dam = metros/10
hm = metros/100
km = metros/1000
print('\n O valor {} está em metros.\n Sua conversão em centímetros fica {:.0f}cm, e em milímetros fica {:.0f}mm!'.format(metros,centimetros,milimetros))
print(' Também possui {:.0f} dm, {} dam, {} hm e {} km.'.format(dm,dam,hm,km))


