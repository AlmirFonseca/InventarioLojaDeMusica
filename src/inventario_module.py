import pandas as pd

def listar(inventario):
    ''' Função de listagem de itens do inventário
    
    Dado um inventário, retorna os itens do inventário.

    :param inventario: Dataframe do inventário
    :type inventario: pandas.core.frame.DataFrame
    :rtype: pd.DataFrame
    
    '''
    
    return inventario

def adicionar(inventario, nome, quantidade):
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
    
    inventario.iloc[-1] = [nome, quantidade]
    
    return inventario
    
def remover(inventario, indice):
    ''' Função de remover itens do inventário
    
    Dado um inventário e o índice de um item, a função remove o item do inventário.
    Caso o índice indicado não corresponda a nenhum item, uma mensagem de erro é impressa.
    Por fim, a função retorna o inventário atualizado

    :param inventario: Dataframe do inventário
    :type inventario: pandas.core.frame.DataFrame
    :param indice: Índice do produto a ser removido
    :type indice: int
    :rtype:pandas.core.frame.DataFrame
    
    '''

    try:
        inventario = inventario.drop(index = indice)
    except:
        print(f"O índice indicado ({indice}) não corresponde a nenhum item do inventário da nossa loja de música")
    inventario.reset_index(drop=True, inplace=True)
    
    return inventario

