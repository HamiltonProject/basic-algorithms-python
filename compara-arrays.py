# Retornar interseção entre os dois arrays

array_base = [0,1, 1, 2, 3, 5, 8, 13, 21]
array_comparacao = [1, 2, 3]

#Retornar 1, 2 e 3

for indice_base in array_base:
    for indice_comparacao in array_comparacao:
        if indice_base == indice_comparacao:
            print(indice_base)
            break