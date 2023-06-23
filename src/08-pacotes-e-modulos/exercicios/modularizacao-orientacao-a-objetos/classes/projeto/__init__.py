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