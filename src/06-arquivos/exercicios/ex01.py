"""  crie a função carregar_dados_alunos que recebe como parâmetro 
o nome de um arquivo que contém dados de alunos e retorna uma tupla,
onde cada elemento é um dicionário com as seguintes chaves: 
prontuario, nome e email """

def carregar_dados_alunos(dados_alunos):
    with open(dados_alunos, 'r', encoding='utf-8') as dados_alunos:
        lista_tupla = []
        for dados in dados_alunos:
            infos = dados.split(sep=',')
            prontuario, nome, email = infos
            dict_aluno = {
                'prontuario': prontuario,
                'nome': nome,
                'email': nome
            }
            lista_tupla.append(dict_aluno)
    tupla_dict = (lista_tupla)
    return(tupla_dict)
   
tupla_alunos = carregar_dados_alunos('dados_aluno.txt')

for aluno in tupla_alunos:
    print('{')
    #print('}')
    for key, value in aluno.items():
        print(f'    {key} : {value}')
    print('}')
