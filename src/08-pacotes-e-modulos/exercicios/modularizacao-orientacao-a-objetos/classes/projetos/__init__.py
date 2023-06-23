class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
    
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if not value:
            raise ValueError('O código não pode ser vazio!!')
        self._codigo = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError('O título não pode ser vazio!!')
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError('O nome do professor responsável não pode ser vazio!!')
        self._responsavel = value

    def __eq__(self, value):
        if isinstance(value, Projeto):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __repr__(self):
        return f'{self.codigo},{self.titulo},{self.responsavel}'

    @classmethod
    def from_string(cls, projeto_string):
        codigo, titulo, responsavel = projeto_string.split(",")
        return cls(codigo, titulo, responsavel)

def comparar_codigo(projeto1, projeto2, projeto3):
    projetos = {projeto1, projeto2, projeto3}

    if len(projetos) == 3:
        print('Os códigos são diferentes.')
        print(projetos)

    elif len(projetos) == 2:
        print('Dois códigos são iguais!!')
        print('Projetos com códigos diferentes:')

        if projeto1 != projeto2:
            print(projeto1)
        if projeto1 != projeto3:
            print(projeto3)
        if projeto2 != projeto3:
            print(projeto2)

    else:
        print('Todos os códigos são iguais!!')