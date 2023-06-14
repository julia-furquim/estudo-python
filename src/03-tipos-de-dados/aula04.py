""" Aula 04 - Dicts """

# Dic (dicionario)
# coleção de key-value
# a key é única
# mutável

#criar um dict
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
    }
print(carro, type(carro))

#acessar valores por chave
print(carro["marca"])
print(carro.get("marca"))

# pegar todas as chaves, valores, pares
print(carro.keys())
print(carro.values())
print(carro.items())

#verifica se a chave existe
print("cor" in carro)

# adicionar chave/ valor de forma dinâmica
carro["cor"] = 'azul'
print("cor" in carro)
print(carro, type(carro))

#remove a chave 
marca = carro.pop("marca")
print(marca)
print(carro)

#loop
for key in carro:
    print(key, carro[key], type[key])

for value in carro.values():
    print(value)    

for key in carro.keys():
    print(key)        

print(carro.items())


for key, value in carro.items():
    print(key, value)

#lista de dicionários

aluno1 = {
    'nome' : 'João',
    'email' : 'joao@email.com',
    'notas' : [10.0, 5.3, 7.0]
}  

aluno2 = {
    'nome' : 'Maria',
    'email' : 'maria@email.com',
    'notas' : [10.0, 2.3, 10.0]
}  

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)