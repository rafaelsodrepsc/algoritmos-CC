#18.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7 * altura) – 58.

from tratamentoErro import *

altura = float(erroVirgula(input("Digite sua altura (em metros): ")))

peso_ideal = (72.7 * altura) - 58

print('O peso ideal para uma pessoa de {} m de altura é de {:.2f} kg'.format(altura,peso_ideal))