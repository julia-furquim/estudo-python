def metade(p):
    return p / 2

def dobro(p):
    return p * 2

def aumentar(p, aumento):
    return p + (aumento/100 * p)

def diminuir(p, desconto):
    return p - (desconto/100 * p)

def moeda(p, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')
