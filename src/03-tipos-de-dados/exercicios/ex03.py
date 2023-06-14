""" - [ ]  solicite ao usuário o mês do ano no formato numérico 
1, 2, 3 ..12 e apresente o nome do ano.
- Exemplo: entrada 3 saída ‘Março’.
- **Implementar com Dicionário** """

MESES = {
    1: 'janeiro', 
    2: 'fevereiro', 
    3: 'março', 
    4: 'abril', 
    5: 'maio', 
    6: 'junho',
    7: 'julho', 
    8: 'agosto', 
    9: 'setembro', 
    10: 'outubro', 
    11: 'novembro', 
    12: 'dezembro'
    }

MES = int(input('Qual o mês em que estamos(formato numérico):'))

if 1 < MES > 12:
    print('O número digitado deve estar entre 1 e 12!')
else:
    for key, value in MESES.items():
        if key == MES:
            print(f'O mês {key} corresponde a {value}')