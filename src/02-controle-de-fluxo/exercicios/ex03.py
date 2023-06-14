"""" ex03.py O código identificador de funcionários de uma empresa 
contém 7 caracteres, inicia com a sequência de caracteres BR, 
em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza
com o caractere X. Exemplos válidos: BR0001X BR1236X BR9999X; 
Exemplos inválidos: br0001X BR126X BR99999X BR9999Y; 
Crie um programa em python que solicita ao usuário um 
identificador e apresenta se o que foi informado é um 
valor válido ou inválido. """

CODIGO_FUNCIONARIO = input('Insira seu código:')

TAMANHO_VALIDO = len(CODIGO_FUNCIONARIO) == 7
LETRAS_VALIDAS = CODIGO_FUNCIONARIO[0:2] == 'BR' and CODIGO_FUNCIONARIO[-1] == 'X'
NUMEROS_VALIDOS = 1 <= int(CODIGO_FUNCIONARIO[2:6]) <= 9999


if TAMANHO_VALIDO and LETRAS_VALIDAS and NUMEROS_VALIDOS:
    print('Código válido')
else:
    print('Código inválido')