from tratamentoErro import *

num1 = float(erroVirgula(input('Digite o primeiro número: ')))
num2 = float(erroVirgula(input('Digite o segundo número: ')))

print('A soma do número {} e {} é igual a {}'.format(num1, num2, num1+num2))