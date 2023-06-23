""" Modularização do exercício 2 de orientação a obejtos """
from classes import projetos

projeto1 = projetos.Projeto.from_string('1,Projeto Sol,João Pires')
projeto2 = projetos.Projeto.from_string('3,Projeto Lua,Maria Pereira')
projeto3 = projetos.Projeto.from_string('3,Projeto Estrela,Carlos Bragança')

projetos.comparar_codigo(projeto1, projeto2, projeto3)