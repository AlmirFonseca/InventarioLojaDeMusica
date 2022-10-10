import sys

sys.path.insert(0, "./src")

import pandas as pd

import inventario_module as inv

colunas = ["Item", "Quantidade"]
linhas = [["Saxofone", 2], ["Flauta", 7], ["Violão", 5], ["Clarinete", 8], ["Bumbo", 3], ["Contrabaixo", 2], ["Guitarra", 2]]

inventario = pd.DataFrame(data=linhas, columns=colunas)

print("\n", "=-"*10, "FUNÇÃO DE LISTAGEM","=-"*10, "\n")
print("Listando os itens do dicionário...")
print(inv.listar(inventario))

print("\n", "=-"*10, "FUNÇÃO DE ADIÇÃO","=-"*10, "\n")
print("Adicionando uma cítara ao inventário...")
print(inv.adicionar(inventario,"Cítara", 1))

print("\n", "=-"*10, "FUNÇÃO DE REMOÇÃO","=-"*10, "\n")
print("Qual o item de índice 2?\n")
print(inv.remover(inventario, 2))

print("\n")
print("Qual o item de índice 10?\n")
print(inv.remover(inventario, 10))
