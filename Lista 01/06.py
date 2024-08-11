from tratamentoErro import *

lado = float(erroVirgula(input('Digite o valor de um dos lados do quadrado: ')))

area = lado ** 2

print('O valor da area é {:.3f}'.format(area))