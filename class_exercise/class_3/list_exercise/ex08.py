# #9. Validador de Tuplas em Conjuntos (Set & Tuple)
# Peça ao usuário pares de coordenadas (x, y). Como listas não podem ser itens de um Set, você
# deve:
# ● Armazenar cada par em uma Tuple.
# ● Adicionar as tuplas a um Set.
# ● Se o usuário tentar inserir uma coordenada que já existe, o programa deve avisar:
# "Coordenada duplicada ignorada".
# ● Ao final, exiba a distância total percorrida entre todos os pontos únicos.

sum = 0
for number in range(1, 101):
    sum = sum + number

print(f" A soma é: {sum}")
    