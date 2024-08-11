from tratamentoErro import *

ganhoHora = float(erroVirgula(input('Digite o valor ganho por hora: ')))
horasTrab = float(erroVirgula(input('Digite o número de horas trabalhadas: ')))

salario = ganhoHora * horasTrab
Ir = salario * (11/100)
Inss = salario * (8/100)
Sindicato = salario * (5/100)
salarioLiquido = salario - Ir - Inss - Sindicato

print('''
Salário Bruto : R$ {}
IR (11%) : R$ {}
INSS (8%) : R$ {}
Sindicato ( 5%) : R$ {}
Salário Liquido : R$ {}
'''.format(salario, Ir, Inss, Sindicato, salarioLiquido))