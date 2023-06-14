"""  - [ ]  `ex02.py` solicite ao usuário o mês do ano no 
formato numérico 1, 2, 3 ..12 e apresente o nome do ano.
- Exemplo: entrada 3 saída ‘Março’.
- **Implementar com Tupla** """

MESES = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
MES = int(input('Qual o mês em que estamos(formato numérico):'))

if 1 < MES > 12:
    print('O número digitado deve estar entre 1 e 12!')
else:
    print(f'O mês {MES} corresponde a', MESES[MES-1])
    




