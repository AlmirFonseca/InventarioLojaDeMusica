#inventario

import pandas as pd

dic = {"hello":20}

def listar(inventario):
    ''' Função de listagem de itens do inventário
    
    Dado um inventário, retorna os itens do inventário.

    :param inventario: Dataframe do inventário
    :type inventario: pandas.core.frame.DataFrame
    :rtype: pd.DataFrame
    
    '''
    return inventario

def adicionar(inventario,nome, quantidade):
    ''' Função de adição de itens no inventário
    
    Dado um inventário e dados de um novo produto (nome e quantidade), insere o novo produto no inventário da loja de música e retorna o inventário atualizado

    :param inventario: Dataframe do inventário
    :type inventario: pandas.core.frame.DataFrame
    :param nome: nome do produto a ser adicionado
    :type nome: str
    :param quantidade: quantidade do produto
    :type quantidade: int
    :rtype: pandas.core.frame.DataFrame
    
    '''
    return inventario
    
def remover(dicionario, indice):
    ''' Função de remover itens do inventário
    
    Dado um inventário e o índice de um item, a função remove o item do inventário.
    Caso o índice indicado não corresponda a nenhum item, uma mensagem de erro é impressa.
    Por fim, a função retorna o inventário atualizado

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

