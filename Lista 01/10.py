#Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). 
#O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.

from tratamentoErro import *

#import json
#import requests

#linkC = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
#cotacao = linkC.json()

dolar = float(erroVirgula(input('Digite quantos Dólares vão ser convertidos para Real: R$')))
cotacao = float(erroVirgula(input('Digite a cotação do Dolar: ')))

real = dolar * cotacao

print('o valor em real é R${}'.format(real))

