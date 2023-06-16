"""  crie uma função que recebe vários argumentos numéricos 
através do *args retorna a soma dos números """
breakpoint()
def somar(*numeros):
    soma = 0.0
    for numero in numeros:
        soma += numero
    return soma

print('O resultado da soma dos números é igual a', somar(10.0, 5.5, 8.0, 2.3, 10.5, 6.0))