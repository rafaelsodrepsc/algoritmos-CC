#20.	Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o 
# valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.

from tratamentoErro import *

A = float(erroVirgula(input('Digite um valor para A: ')))
B = float(erroVirgula(input('Digite um valor para B: ')))

A,B = B,A

print('O valor de A é {} e o valor de B é {}'.format(A,B))