#14.	Escrever um algoritmo para determinar o consumo médio de um automóvel 
# sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.

from tratamentoErro import *

distanciaP = float(erroVirgula(input('Digite a distancia percorrida (em km) pelo automóvel: ')))
combustivelG = float(erroVirgula(input('Digite quanto de combustivel foi gasto (em litros) nesse trajeto: ')))

consumoMed = distanciaP / combustivelG

print('O consumo médio é igual a {} km/l'.format(consumoMed))