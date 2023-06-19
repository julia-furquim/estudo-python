""" Aula 02 - atributos de classe e instância """

# classe Pessoa possui:
# atributos de instância: nome e email
# atributos de classe: espécie

class Pessoa:
    especie = 'Humano'

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


pessoa1 = Pessoa('Maria da Silva', "maria@email.com")
pessoa2 = Pessoa('João Santos', 'joao@email.com')
pessoa3 = Pessoa('Pedro Souza', 'pedro@email.com')

# alterar um atributo de classe na instância (objeto)
# altera somente para aquela instância
pessoa1.especie = 'Alienígena'

# alterando umj atributo da classe na classe
# altera todos os objetos e na classe também
Pessoa.especie = 'Alienígenas do passado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print(pessoa3.nome, pessoa3.email, pessoa3.especie)

print(Pessoa.especie)