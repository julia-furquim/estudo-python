""" crie uma função que recebe uma tupla 
de números como parâmetro (numeros) e retorna a soma dos números """

breakpoint()
def somar(numeros):
    soma = 0.0
    for numero in numeros:
        soma += numero
    return soma

numeros_tupla = (10.0, 5.5, 8.0, 2.3, 10.5, 6.0)

print('O resultado da soma dos números da tupla é igual a',somar(numeros_tupla))