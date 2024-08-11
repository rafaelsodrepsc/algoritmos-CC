#11.	Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. 
# Considere fixo o juro da poupança em 0,70% a. m.

from tratamentoErro import *

valorDeposito = float(erroVirgula(input('Digite o valor que deseja depositar: ')))

rendimentoTotal = valorDeposito + (valorDeposito * (0.7/100))

print("o rendimento de {} com taxa de 0,7% ao mês é igual a: {}".format(valorDeposito,rendimentoTotal))

