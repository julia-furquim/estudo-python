""" Calculadora IMC """

print('-----------------------------------')
print('IMC            Classificação')
print('-----------------------------------')

individuo = { }

altura = float(input('Insira sua altura em metros:'))
peso = float(input('Insira seu peso em Kg:')) 

individuo = {
     'altura': altura,
     'peso': peso
 }

print(individuo)

def calcular_imc(individuo):
    imc = individuo['peso'] / (individuo['altura'] * individuo['altura'])
    return(imc)

def obter_classificacao(imc):
    BAIXO_PESO =  imc < 18.5
    PESO_NORMAL = 18.5 >= imc <= 24.9
    EXCESSO_PESO = 25.0 >= imc <= 29.9
    OBESIDADE1 = 30.0 >= imc <= 34.9
    OBESIDADE2 =  35.0 >= imc <= 39.9
    OBESIDADE3 = imc >= 40.0

    if BAIXO_PESO:
        return 'Baixo peso'
    elif PESO_NORMAL:
        return 'Peso normal'
    elif EXCESSO_PESO:
        return 'Excesso de peso'
    elif OBESIDADE1:
        return 'Obesidade de Classe 1'
    elif OBESIDADE2:
        return 'Obesidade de Classe 2' 
    elif OBESIDADE3:
        return 'Obesidade de Classe 3'

def situacao_individuo(imc):
    if imc < 18.5:
        return 'Ganhar peso'
    elif 18.5 >= imc <= 24.9:
        return 'Peso normal' 
    else:
        return 'Perder peso'
    
imc = calcular_imc(individuo)
classificacao = obter_classificacao(imc)
situacao = situacao_individuo(imc)

print('Com base na altura e o peso informados, o IMC é')
print('------', imc, '------')
print('Você está com', classificacao, '!!')
print('Baseado nisso, a recomendação é:')
print('------', situacao, '------')