class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email
    
    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if not value:
            raise ValueError('O prontuário não pode ser vazio!!')
        self._prontuario = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError('O nome não pode ser vazio!!')
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError('O email não pode ser vazio!!')
        self._email = value

    def __eq__(self, value):
        if isinstance(value, Aluno):
            return self.prontuario == value.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)

    def __repr__(self):
        return f'{self.prontuario},{self.nome},{self.email}'

    @classmethod
    def from_string(cls, aluno_string):
        prontuario, nome, email = aluno_string.split(",")
        return cls(prontuario, nome, email)

def comparar_prontuario(aluno1, aluno2, aluno3):
    alunos = {aluno1, aluno2, aluno3}

    if len(alunos) == 3:
        print('Os prontuários são diferentes.')

    elif len(alunos) == 2:
        print('Dois prontuários são iguais!!')
        print('Alunos com prontuários diferentes:')

        if aluno1 != aluno2:
            print(aluno1)
        if aluno1 != aluno3:
            print(aluno3)
        if aluno2 != aluno3:
            print(aluno2)

    else:
        print('Todos os prontuários são iguais!!')