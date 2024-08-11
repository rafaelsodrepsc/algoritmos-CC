from tratamentoErro import *

nota1 = float(erroVirgula(input('Digite a primeira nota: ')))
nota2 = float(erroVirgula(input('Digite a segunda nota: ')))
nota3 = float(erroVirgula(input('Digite a terceira nota: ')))
nota4 = float(erroVirgula(input('Digite a quarta nota: ')))

media = (nota1 + nota2 + nota3 + nota4)/4
    
print('A media é igual a {}'.format(media))

    
    