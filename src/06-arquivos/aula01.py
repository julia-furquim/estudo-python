""" Aula 01 - Arquivos """

# open("caminho", "r")

# Mode
# r - leitura
# a - append / incrementar
# w - escrita
# x - criar arquivo
# r+ - leitura + escrita

# arquivo = open('teste3.txt', 'x',  encoding='utf-8')

# print(arquivo.readable())
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines()
# print(lista)

# print(lista[3])


# arquivo.write("C\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")
# arquivo.write("Python\n")

import os

# if os.path.exists('teste2.txt'):
#     os.remove('teste2.txt')
# else:
#     print('Arquivo não existe')
os.rmdir('nova_pasta')

# arquivo.close() 