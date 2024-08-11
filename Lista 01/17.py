#17.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
#•	o produto do dobro do primeiro com metade do segundo . 
#•	a soma do triplo do primeiro com o terceiro.     
#•	o terceiro elevado ao cubo. 

from tratamentoErro import *
 
inteiro1 = int(input('Digite o primeiro inteiro: '))
inteiro2 = int(input('Digite o primeiro segundo: '))
real = float(erroVirgula(input('Digite um numero pertencente aos reais: ')))

calculo1 = (2 * inteiro1) * (inteiro2 / 2)
calculo2 = (3 * inteiro1) + real
calculo3 = pow(real,3)

print('''
- o produto do dobro do primeiro com metade do segundo é igual a {}
- a soma do triplo do primeiro com o terceiro é igual a {}     
- o terceiro elevado ao cubo é igual a {}
'''.format(calculo1, calculo2, calculo3 ))