""" Cálculo - aquário """
breakpoint()
print('-----------------------------------')
print('.............AQUÁRIO...............')
print('-----------------------------------')

comprimento = float(input('Insira o comprimento do aquário:'))
altura = float(input('Insira a altura do aquário:'))
largura = float(input('Insira a largura do aquário:'))
temp_ambiente = float(input('Insira a temperatura ambiente:'))
temp_desejada = float(input('Insira a temperatura desejada:'))

def calculo_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000
    
volume = calculo_volume(comprimento, altura, largura)
 

def calculo_potencia(volume, temp_desejada, temp_ambiente):
    potencia = (volume * 0.05) * (temp_desejada - temp_ambiente)
    return (potencia)

potencia = calculo_potencia(volume, temp_desejada, temp_ambiente)

def calculo_filtragem(volume):
    filtragem_min = volume * 2
    filtragem_max = volume * 3
    return f'A filtragem por hora deve estar entre {filtragem_min} e {filtragem_max}'

filtragem = calculo_filtragem(volume)


print('O volume do aquário é:', volume)
print('A potência do termostato é:', potencia)
print(filtragem)