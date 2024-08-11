#16.	Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas 
# por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, 
# o salário fixo e salário no final do mês.

from tratamentoErro import *

nome = input("Digite o nome do vendedor: ")
salario = float(input('Digite seu salario fixo: '))
vendasFeitas = int(input('Digite o total de vendas realizadas no mês: '))

comissao = vendasFeitas * (15/100)

print('''\nRelatorio mensal do vendedor {}
salario fixo mensal é de {}
salario ao final com comissão é de {}
'''.format(nome,salario, salario+comissao))
