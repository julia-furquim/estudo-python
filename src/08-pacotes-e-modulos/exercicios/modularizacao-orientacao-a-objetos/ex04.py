""" Modularização do exercício 4 de orientação a obejtos """

from classes import aluno, projeto, participacao

aluno1 = aluno.Aluno.from_string('SP0101,João da Silva,joao@gmail.com')
aluno2 = aluno.Aluno.from_string('SP0103,Maria Souza,maria@gmail.com')
aluno3 = aluno.Aluno.from_string('SP0102,Carlos Santos,carlos@gmail.com')

projeto1 = projeto.Projeto.from_string('1,Projeto Sol,João Pires')
projeto2 = projeto.Projeto.from_string('2,Projeto Lua,Maria Pereira')
projeto3 = projeto.Projeto.from_string('3,Projeto Estrela,Carlos Bragança')

participacao1 = participacao.Participacao('1', '2022-01-01', '2022-06-30', aluno1, projeto1)
participacao2 = participacao.Participacao('2', '2022-03-15', '2022-12-31', aluno2, projeto2)
participacao3 = participacao.Participacao('3', '2022-02-01', '2022-08-31', aluno3, projeto3)

projeto1.add_participacao(participacao1)
projeto2.add_participacao(participacao2)
projeto3.add_participacao(participacao3)

print(participacao1)
print(participacao2)
print(participacao3)

print(projeto1.participacoes)
print(projeto2.participacoes)
print(projeto3.participacoes)