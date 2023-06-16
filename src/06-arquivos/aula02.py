""" Aula 02 - Manipulando arquivos com Python """

# arq = open('arquivo.txt', 'w')


# # x = ['Júlia', 'Helena', 'Juliana']

# # for nome in x:
# #     arq.write(nome + '\n')
# # # arq.writelines()

# arq.close()

# with open('arquivo.txt', 'a') as arq:
#     arq.write("\njúlia")

# with open('arquivo.txt', 'r') as arq:
#     x = arq.read()
#     print(type(x))

# with open('arquivo.txt', 'r') as arq:
#     x = arq.readlines()
#     print(type(x))

# with open('arquivo.txt', 'rb') as arq:
#     x = arq.read()
#     print(type(x.decode))

# with open('arquivo.txt', 'r') as arq:
#     for i in arq:
#         print(i)

with open('arquivo.txt', 'r') as arq:
    for i in arq:
        print(next(arq))


   