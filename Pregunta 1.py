# Lista para almacenar los números que cumplen con las condiciones
numeros_cumplen = []

# Iterar sobre el rango de 1500 a 2700 (ambos incluidos)
for num in range(1500, 2701):
    # Verificar si el número es divisible por 7 y múltiplo de 5
    if num % 7 == 0 and num % 5 == 0:
        # Si cumple, agregarlo a la lista
        numeros_cumplen.append(num)

# Imprimir los números que cumplen con las condiciones
print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros_cumplen)
