""" Modularização do exercício 3 de orientação a obejtos """
from classes import aluno, projetos, participacao

aluno1 = aluno.Aluno.from_string('SP0101,João da Silva,joao@gmail.com')
aluno2 = aluno.Aluno.from_string('SP0101,Maria Souza,maria@gmail.com')
aluno3 = aluno.Aluno.from_string('SP0102,Carlos Santos,carlos@gmail.com')

projeto1 = projetos.Projeto.from_string('1,Projeto Sol,João Pires')
projeto2 = projetos.Projeto.from_string('3,Projeto Lua,Maria Pereira')
projeto3 = projetos.Projeto.from_string('3,Projeto Estrela,Carlos Bragança')

participacao1 = participacao.Participacao("1", "2022-01-01", "2022-06-30", aluno1, projeto1)
participacao2 = participacao.Participacao("2", "2022-03-15", "2022-12-31", aluno2, projeto2)
participacao3 = participacao.Participacao("3", "2022-02-01", "2022-08-31", aluno3, projeto3)

print(participacao1)
print(participacao2)
print(participacao3)


# def comparar_codigo(projeto1, projeto2, projeto3):
#     projetos = {projeto1, projeto2, projeto3}

#     if len(projetos) == 3:
#         print('Os códigos são diferentes.')
#         print(projetos)

#     elif len(projetos) == 2:
#         print('Dois códigos são iguais!!')
#         print('Projetos com códigos diferentes:')

#         if projeto1 != projeto2:
#             print(projeto1)
#         if projeto1 != projeto3:
#             print(projeto3)
#         if projeto2 != projeto3:
#             print(projeto2)

#     else:
#         print('Todos os códigos são iguais!!')


projetos.comparar_codigo(projeto1, projeto2, projeto3)


# def comparar_prontuario(aluno1, aluno2, aluno3):
#     alunos = {aluno1, aluno2, aluno3}

#     if len(alunos) == 3:
#         print('Os prontuários são diferentes.')

#     elif len(alunos) == 2:
#         print('Dois prontuários são iguais!!')
#         print('Alunos com prontuários diferentes:')

#         if aluno1 != aluno2:
#             print(aluno1)
#         if aluno1 != aluno3:
#             print(aluno3)
#         if aluno2 != aluno3:
#             print(aluno2)

#     else:
#         print('Todos os prontuários são iguais!!')


aluno.comparar_prontuario(aluno1, aluno2, aluno3)
    