class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    def obtem_nome(self):
        return self.nome

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if not value:
            raise ValueError('O prontuário não pode ser vazio!')
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError('O nome não pode ser vazio!')
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError('O email não pode ser vazio!')
        self._email = value

    def __eq__(self, other):
        if isinstance(other, Aluno):
            return self.prontuario == other.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)

    def __repr__(self):
        return f'Aluno(prontuario={self.prontuario}, nome={self.nome}, email={self.email})'

    @classmethod
    def from_string(cls, aluno_string):
        prontuario, nome, email = aluno_string.split(",")
        return cls(prontuario, nome, email)


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    def obtem_titulo(self):
        return self.titulo

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if not value:
            raise ValueError('O código não pode ser vazio!')
        self._codigo = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError('O título não pode ser vazio!')
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError('O nome do professor responsável não pode ser vazio!')
        self._responsavel = value

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

    def __eq__(self, other):
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __repr__(self):
        return f'Projeto(codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel})'

    @classmethod
    def from_string(cls, projeto_string):
        codigo, titulo, responsavel = projeto_string.split(",")
        return cls(codigo, titulo, responsavel)

class Participacao(Projeto, Aluno):
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        Projeto.__init__(self, codigo, projeto.titulo, projeto.responsavel)
        Aluno.__init__(self, aluno.prontuario, aluno.nome, aluno.email)
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def __repr__(self):
        aluno_repr = Aluno.__repr__(self)
        projeto_repr = Projeto.__repr__(self)
        return f'Participacao(codigo={self.codigo}, data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={aluno_repr}, projeto={projeto_repr})'

aluno1 = Aluno.from_string('SP0101,João da Silva,joao@gmail.com')
aluno2 = Aluno.from_string('SP0103,Maria Souza,maria@gmail.com')
aluno3 = Aluno.from_string('SP0102,Carlos Santos,carlos@gmail.com')

projeto1 = Projeto.from_string('1,Projeto Sol,João Pires')
projeto2 = Projeto.from_string('2,Projeto Lua,Maria Pereira')
projeto3 = Projeto.from_string('3,Projeto Estrela,Carlos Bragança')

participacao1 = Participacao('1', '2022-01-01', '2022-06-30', aluno1, projeto1)
participacao2 = Participacao('2', '2022-03-15', '2022-12-31', aluno2, projeto2)
participacao3 = Participacao('3', '2022-02-01', '2022-08-31', aluno3, projeto3)

projeto1.add_participacao(participacao1)
projeto2.add_participacao(participacao2)
projeto3.add_participacao(participacao3)

print(participacao1)
print(participacao2)
print(participacao3)

print(projeto1.participacoes)
print(projeto2.participacoes)
print(projeto3.participacoes)