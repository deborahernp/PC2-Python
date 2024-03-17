# Número de filas del patrón (se puede ajustar según sea necesario)
num_filas = 5

# Imprimir la parte superior del patrón
for i in range(num_filas):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# Imprimir la parte inferior del patrón
for i in range(num_filas - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()