""" - [ ]  `ex04.py` Implemente o `ex03.py` mas ao final do 
programa deve ser apresentado ao usuário todos os problemas que 
o identificador informado possui (implementar como list de erros):
- Ex: identificador informado: B9999999X
- erros
- O identificar não inicia com a sequencias ‘BR’
- O identificador não apresenta números inteiros entre 
0001 e 9999- Ex: identificador informado: BR9999Y
- erros
- O identificar não finaliza com o caracter X """


CODIGO_FUNCIONARIO = input('Insira seu código:')
ERROS = []

TAMANHO_VALIDO = len(CODIGO_FUNCIONARIO) == 7
LETRAS_VALIDAS = CODIGO_FUNCIONARIO[0:2] == 'BR' and CODIGO_FUNCIONARIO[-1] == 'X'
NUMEROS_VALIDOS = 1 <= int(CODIGO_FUNCIONARIO[2:6]) <= 9999 



if not TAMANHO_VALIDO:
    ERROS.append('Erro!! A quantidade de caracteres do código identificador deve ser 7')
if not LETRAS_VALIDAS:
    ERROS.append('O código identificador deve iniciar com as letras BR e terminar com a letra X \nTODAS AS LETRAS DO CÓDIGO, DEVEM SER MAIÚSCULAS!!!')
if not NUMEROS_VALIDOS:
    ERROS.append('Os números do código devem estar entre 0001 e 9999:')

if ERROS:
    print('Verifique os erros encontrados no seu código e tente novamente')
    for ERRO in ERROS:
        print(ERRO, sep='\n')
else:
    print('O código identificador digitado, é válido!')