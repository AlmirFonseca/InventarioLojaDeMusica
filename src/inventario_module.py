#inventario

import pandas as pd

dic = {"hello":20}

def listar(inventario):
    ''' Função de que lista itens do inventário

    :param inventario: Dataframe do inventário
    :type inventario: pandas.core.frame.DataFrame
    :rtype: pd.DataFrame
    
    '''
    return inventario

def adicionar(inventario,nome, quantidade):
    ''' Função que adiciona item ao inventário 

    :param inventario: Dataframe do inventário
    :type inventario: pandas.core.frame.DataFrame
    :param nome: nome do produto a ser adicionado
    :type nome: str
    :param quantidade: quantidade do produto
    :type quantidade: int
    :rtype: pandas.core.frame.DataFrame
    
    '''
    return inventario
    
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


