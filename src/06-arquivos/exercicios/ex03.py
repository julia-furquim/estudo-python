""" com base nos códigos dos exercícios anteriores, crie a função 
linha_para_dict que recebe uma linha do arquivo (string), 
exemplo SP000001,Maria da Silva,maria@email.com , uma lista com 
os nomes das chaves do dicionário ['prontuario', 'nome', 'email'] 
e retorna o dicionário correspondente à aquele registro.  """

def linha_para_dict(linha, chaves):
    valores = linha.strip().split(',')
    dicionario = {}
    for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i].strip()
    return dicionario

def buscar_dados(dados_dict, dados_dict_2):
    with open(dados_dict_2, 'r', encoding='utf-8') as arquivo2:
        linhas = arquivo2.readlines()
        if len(linhas) >= 2:
            chaves = linhas[0].strip().split(',')
            valores = linhas[1].strip().split(',')
            with open(dados_dict, 'r', encoding='utf-8') as arquivo1:
                for linha in arquivo1:
                    if all(valor.strip() in linha for valor in valores):
                        return linha_para_dict(linha, chaves)

    return None

keys = ['prontuario', 'nome', 'email']
data = 'SP000001,Maria da Silva,maria@email.com'

result = buscar_dados('dados_dict.txt', 'dados_dict_2.txt')
if result:
    print('{')
    for key, value in result.items():
        print(f'    {key} : {value}')
    print('}')
else:
    print('Registro não encontrado.')

