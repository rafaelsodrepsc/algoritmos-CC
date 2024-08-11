#12.	A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros.
#  Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.

from tratamentoErro import *

valorComp = float(erroVirgula(input("Digite o valor da compra: ")))

print(''' ============Prestações==============
Dividido em 1x sem juros - 1x {:.2f}
Dividido em 2x sem juros - 2x {:.2f}
Dividido em 3x sem juros - 3x {:.2f}
Dividido em 4x sem juros - 4x {:.2f}
Dividido em 5x sem juros - 5x {:.2f}
      '''.format(valorComp, valorComp/2, valorComp/3, valorComp/4, valorComp/5))