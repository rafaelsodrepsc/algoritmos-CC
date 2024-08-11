from tratamentoErro import *
import math

raioC = float(erroVirgula(input('Digite o raio do circulo: ')))

areaC = math.pi * (raioC**2)

print('O valor da área é: {:.4f}'.format(areaC))