""" Aula 05 - métodos especiais """

# __str__(self)
# representação de objeto como string para humanos

# __repr__(self)
# representação de objeto como string para recriar esse  objeto
# representação canônica
# logging, debug

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def  calcular_area(self):
        return self.base * self.altura   
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    

    # __str__(self)
    # representação de objeto como string para humanos
    def __str__(self):
        return f'Retangulo[base={self.base}, altura={self.altura}]'
    
    # __repr__(self)
    # representação de objeto como string para recriar esse  objeto
    # representação canônica
    # logging, debug
    def __repr__(self):
        return f'Retangulo({self.base},{self.altura})'

retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(3.0, 14.0)

# representacao_string_retangulo = 'Retangulo(7.5,12.3)'
# print(retangulo1.__repr__())

retangulo3 = eval('Retangulo(7.5,12.3)')
retangulo4 = eval(repr(retangulo3))

print(retangulo1)
print(retangulo2)
print(retangulo3)
print(retangulo4)