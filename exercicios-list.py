# 1 - Lista de números de 1 a 20.
list_numbers = [number for number in range(1, 21)]
print(list_numbers)

# Crie uma lista com números de 1 a um milhão e, em seguida,
# use min() e max() a fim de garantir que sua lista realmente
# comece em um e termine em um milhão. Além disso, use a 
# função sum() para ver a rapidez com que o pyhton efetua
# a soma de um milhão de números.
list = [number for number in range(1, 1_000_001)]
print(f"Menor número: {min(list)}")
print(f"Maior número: {max(list)}")
sum = sum(list)
print(f"A soma dos números é: {sum}")

# Use o terceiro argumento da função range()
# para criar uma lista com números ímpares
# de 1 a 20. Use o loop for para exibir
# cada número.
odd_list = [odd for odd in range(1, 21, 2)]
print(odd_list)

# Crie uma lista de múltiplos de 3, de 3 a 30.
multiples_of_3 = [numero for numero in range(3, 31) if numero % 3 == 0]
print(multiples_of_3)

# Escreva uma lista dos primeiros 10 cubos (ou seja, o cubo de cada número
# inteiro de 1 a 10) e use um loop for para exibir o valor de cada cubo.
cubes = []
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)
print(cubes)

# Usando list comprehension para gerar uma lista com os primeiros 10 cubos.
cubos = [numero ** 3 for numero in range(1, 11)]