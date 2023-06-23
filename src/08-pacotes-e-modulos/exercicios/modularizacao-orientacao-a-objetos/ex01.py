from classes import aluno

aluno1 = aluno.Aluno.from_string('SP0101,João da Silva,joao@gmail.com')
aluno2 = aluno.Aluno.from_string('SP0101,Maria Souza,maria@gmail.com')
aluno3 = aluno.Aluno.from_string('SP0102,Carlos Santos,carlos@gmail.com')

aluno.comparar_prontuario(aluno1, aluno2, aluno3)