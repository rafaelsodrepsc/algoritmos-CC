from tratamentoErro import *

a = int(input('Digite um número inteiro referente ao A: '))
b = int(input('Digite um número inteiro referente ao B: '))
c = int(input('Digite um número inteiro referente ao C: '))

R = pow((a+b),2)
S = pow((b+c),2)

D = (R + S) / 2

print('O valor de D é igual a {}'.format(D))