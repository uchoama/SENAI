estoque = ["caneca", "caderno", "borracha", "lapis"]

#Adicionar novo item ao estoque
estoque.append("marcador")
print(estoque)

#Remover item do estoque 
estoque.remove("lapis")
print(estoque)

# Veificar se um item está em estoque
print("borracha" in estoque) # Saída: True
