""" crie a função carregar_dados_projetos que recebe como parâmetro
 o nome de um arquivo que contém dados de projetos e retorna uma 
 tupla, onde cada elemento é um dicionário com as seguintes chaves:
codigo (número inteiro que representa o código do projeto), 
titulo e responsável (nome do professor responsável pelo projeto).
Não utilizar bibliotecas ou funções prontas para leitura do arquivo. """

def carregar_dados_projetos(dados_projetos):
    with open(dados_projetos, 'r', encoding='utf-8') as dados_projetos:
        lista_tupla = []
        for dados in dados_projetos:
            infos = dados.split(sep=',')
            codigo, titulo, responsavel = infos
            dict_projeto = {
                'codigo': codigo,
                'titulo': titulo,
                'responsavel': responsavel
            }
            lista_tupla.append(dict_projeto)
    tupla_dict = (lista_tupla)
    return(tupla_dict)
   
tupla_projetos = carregar_dados_projetos('dados_projeto.txt')

for projeto in tupla_projetos:
    print('{')
    #print('}')
    for key, value in projeto.items():
        print(f'    {key} : {value}')
    print('}')