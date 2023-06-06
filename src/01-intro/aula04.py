""" Aula 04 - constantes, variáveis e literais"""

#Variável: container para guardar dados
#inferência de tipo

numero = 10
print(numero, type(numero))
#alterar valor de variável
numero = 20
print(numero)

#múltiplas atribuições
nome, idade, endereco = 'Júlia', 19, 'Rua Oliveira'
print(nome, idade, endereco)

#atribui o mesmo valor para várias variáveis
nome1 = nome2 = nome3 = 'Helena'
print(nome1, nome2, nome3)

nome3= 'Juliana'
print(nome1, nome2, nome3)

#Variáveis
#snake_case
id_funcionario = 209
salario_atual = 5000.50

#Constantes
#Upper case - snake_case
PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18
print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

#Literais
idade = 27
print(idade)
print(27)

#Numéricos 
print(10, type(10))
print(10, type(-10))
print(10.5, type(10.5))

#String
print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("John's house")
print('O filme estava "excelente"')

#Booleano
print(True, type(True))
print(False, type(False))

#None
print(None, type(None))

#Coleções

#Lista(list)
numeros = [1, 2, 3]
print(numeros, type(numeros))

#Tupla(tuple)
emails = ('juliafurquimj@email.com', '123@email.com')
print(emails, type(emails))

#Conjunto(set)
nomes = {'Júlia', 'Paula', 'Gsbriel', 'Paula'}
print(nomes, type(nomes))

#Dicionário(dictionary)
aluno = {
    'prontuario': 304419,
    'nome': 'Júlia',
    'idade': 19
}

print(aluno, type(aluno))