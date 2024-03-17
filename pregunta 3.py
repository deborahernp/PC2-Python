numeros = []  # Lista para almacenar los números ingresados
cantidad_pares = 0
cantidad_impares = 0

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
        
        if numero % 2 == 0:
            cantidad_pares += 1
        else:
            cantidad_impares += 1
    elif respuesta == "NO":
        break
    else:
        print("Respuesta no válida. Por favor, responda SI o NO.")

print("Números ingresados:", numeros)
print("Cantidad de números pares:", cantidad_pares)
print("Cantidad de números impares:", cantidad_impares)