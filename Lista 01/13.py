#1.	Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de 
# custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
from tratamentoErro import *

precoC = float(input('Digite o preço de custo: '))
acrescimo = float(ignorePorcent(input('Digite qual a porcentagem que deve ser acrescida: ')))

precoVenda = precoC + (precoC *(acrescimo/100))

print('O preço de venda é igual a: R$ {}'.format(precoVenda))