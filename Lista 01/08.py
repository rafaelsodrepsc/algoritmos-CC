from tratamentoErro import *

grausF = float(erroVirgula(ignoreGraus((input('Digite a temperatura em Fahrenheit para ser convertido para Celsius: ')))))

grausC = (5*(grausF - 32))/9

print('O valor em Celsius: {}'.format(grausC))
