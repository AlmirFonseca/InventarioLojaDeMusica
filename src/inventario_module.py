#inventario

import pandas as pd

dic = {"hello":20}

def listar(dicionario):
    ''' função de listar 

    :param dicionario: Dicionário que representa o inventário
    :type dicionario: dict
    :param b: segundo numero
    
    :rtype:
    
    '''
    
    inventario = pd.DataFrame(dicionario)
    return inventario

def adicionar(dicionario,item, quantidade):
    ''' função de listar 

    :param dicionario: Dicionário que representa o inventário
    :type dicionario: dict
    :param b: segundo numero
    
    :rtype:
    
    '''
    dicionario[item]=quantidade
    return dicionario
    
def remover(dicionario,item):
    ''' função de listar 

    :param dicionario: Dicionário que representa o inventário
    :type dicionario: dict
    :param b: segundo numero
    
    :rtype:
    
    '''
    dicionario.pop(item)
    return dicionario

def buscar(dicionario,item):
    ''' função de listar 

    :param dicionario: Dicionário que representa o inventário
    :type dicionario: dict
    :param dicionario: Dicionário que representa o inventário
    :type dicionario: dict

    
    :rtype:
    
    '''
    busca = dicionario[item]
    return busca

print(adicionar(dic,"a", 20))
print(remover(dic,"hello"))


