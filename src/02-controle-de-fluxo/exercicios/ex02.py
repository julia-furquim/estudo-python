""" - [ ]  `ex02.py` solicite ao usuário uma única a vez as notas 
no formato `n1, n2, n3, nm` e apresente o resultado da média 
aritmética das notas se está aprovado (maior que 6.0), 
recuperação (entre 4.0 e 6.0) ou reprovado (menor que 4.0).
    - Dica: utilize o método split da classe string para obter 
    as notas como list
    - O programa deve funcionar independente do número de notas 
    informadas pelo usuário, ex: 2 notas `10.0, 3.0` ou 5 notas 
    `10.0, 3.0, 2.0, 5.6, 8.2` """


NOTAS = input('Insira suas notas:')
NOTAS = NOTAS.split(sep=',')

SOMA = 0.0
for NOTA in NOTAS:
    NOTAS_VALIDAS = 0 <= float(NOTA) <= 10
    if NOTAS_VALIDAS:
        SOMA = SOMA + float(NOTA)
    else:
        print('Notas inválidas!')
         

MEDIA = SOMA / len(NOTAS) 
if MEDIA >= 6:
    print('Aprovado')
elif MEDIA >= 4:
    print('Recuperação')
else:
    print('Reprovado')