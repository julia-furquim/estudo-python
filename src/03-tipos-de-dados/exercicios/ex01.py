""" ex01.py solicite ao usuário 3 números, armazene esses
elementos em uma lista e apresente no final o menor e maior 
elemento """

NUMEROS = []

for i in range(3):
    NUMERO = int(input('Insira um número:'))
    NUMEROS.append(NUMERO)

MENOR = NUMEROS[0]
MAIOR = NUMEROS[0]

for NUMERO in NUMEROS:
    if NUMERO > MAIOR:
        MAIOR = NUMERO
    if NUMERO < MENOR:
        MENOR = NUMERO  

print(f'Dentre os números {NUMEROS} digitados, {MENOR} é o menor e {MAIOR} é o maior')          

