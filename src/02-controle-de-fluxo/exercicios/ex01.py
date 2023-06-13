""" ex01.py solicite ao usuário
 3 notas e apresente o resultado
 da média aritmética das notas """

NOTA1 = float(input('Insira a 1º nota: '))
NOTA2 = float(input('Insira a 2º nota: '))
NOTA3 = float(input('Insira a 3º nota: '))


NOTA1_VALIDA = 0 <= NOTA1 <= 10
NOTA2_VALIDA = 0 <= NOTA2 <= 10
NOTA3_VALIDA = 0 <= NOTA3 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA and NOTA3_VALIDA:
    MEDIA = (NOTA1 + NOTA2 + NOTA3) / 2
    mensagem=f'A média das notas: \n {NOTA1}, \n {NOTA2} e \n {NOTA3}, resultou em: \n {MEDIA}'
    print(mensagem)
else:
    print('Notas inválidas')