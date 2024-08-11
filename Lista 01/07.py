from tratamentoErro import *

ganhoH = float(erroVirgula(input('Qual o valor ganho por hora: ')))
HorasTrab = float(erroVirgula(input('Quantas horas foram trabalhadas no mês: ')))

totalSal= HorasTrab * ganhoH

print('O salario ao final do mês é de {}'.format(totalSal))