#9.	Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. 

from tratamentoErro import *

grausC = float(erroVirgula(ignoreGraus((input('Digite a temperatura em Celsius para ser convertido para Fahrenheit: ')))))

grausF = (grausC * 1.8) + 32

print('O valor em Fahrenheit: {}'.format(grausF))