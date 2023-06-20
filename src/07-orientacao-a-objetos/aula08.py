""" Aula 08 - herança entre classes - super() """

class Pessoa: # SUPER CLASSE
    def __init__(self, cpf, nome, sobrenome):           
        # print('Entrei no SUPER CONSTRUTOR')             
        self.cpf = cpf                                  
        self.nome = nome                                
        self.sobrenome = sobrenome                      

    def obtem_nome_completo(self):                      
        return f'{self.nome} {self.sobrenome}'          

class Cliente(Pessoa): # SUB CLASSE
    def __init__(self, cpf, nome, sobrenome):           
        super().__init__(cpf, nome, sobrenome)          
        self.compras = []               

cliente = Cliente('555.666.777-88', 'Júlia', 'Furquim')  
print(cliente.obtem_nome_completo())                    
print(type(cliente))                                   

class Funcionario(Pessoa):
    def __init__(self, cpf, nome, sobrenome, salario):           
        super().__init__(cpf, nome, sobrenome)          
        self.salario = salario

    def calcula_pagamento(self):
        return self.salario - ((10/100)*self.salario)    
    
class Programador(Funcionario):
    def __init__(self, cpf, nome, sobrenome, salario, bonus):           
        super().__init__(cpf, nome, sobrenome, salario)          
        self.bonus = bonus

    def calcula_pagamento(self):
        pagamento_salario = super().calcula_pagamento()  
        return pagamento_salario + self.bonus

funcionario = Funcionario('111.222.333-44', 'Juliana', 'Camargo', 5000.00)
print(funcionario.obtem_nome_completo())
print(funcionario.calcula_pagamento())     

programador = Programador('111.999.555-00', 'Helena', 'Furquim', 5000.00, 200)
print(programador.obtem_nome_completo())
print(programador.calcula_pagamento())     
