# Retornar interseção entre os dois arrays

array_base = [0, 1, 1, 2, 3, 5, 8, 13, 21, 21, 21, 9, 1]
array_comparacao = [1, 2, 3, 9, 10, 100, 2, 11, 1, 9, 2, 3]

# Retornar 1, 2, 3 e 9

# forca bruta
for indice_base in array_base:
    for indice_comparacao in array_comparacao:
        if indice_base == indice_comparacao:
            print(indice_base)
            break
