# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()
# nome.strip()
print(nome.upper())
print(nome.lower())
print('O seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' '))) # mostra a qtd de letras no nome sem a contagem dos espaços
#print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome tem {} letras.'.format(len(separa[0])))















