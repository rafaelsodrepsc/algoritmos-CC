#19.	Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em MBps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

from tratamentoErro import *

tamanhoA = float(erroVirgula(input('Digite o tamanho do arquivo (em MB): ')))
velocidadeI = float(erroVirgula(input('Digite a velocidade da Internet (em MBps): ')))

calculo_tempo = tamanhoA / velocidadeI

tempoMinuto = calculo_tempo / 60

print('O tempo aproximado de download é de {:.3f} minutos'.format(tempoMinuto))