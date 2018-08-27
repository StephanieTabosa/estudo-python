# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip() # transforma tudo em maiúsculo e sem espaços
print('A frase escrita possui {} letras "A".'.format(frase.count('A')))
print('A frase também identificou a primeira letra "A" na posição {}.'.format(frase.find('A')+1)) # para contar normal, começando no 1
print('E a última vez que identificou a letra "A" foi na posição {}.'.format(frase.rfind('A')+1)) #rfind começa do final




