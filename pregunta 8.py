def factorial(numero):
    # El factorial de 0 es 1
    if numero == 0:
        return 1
    # Inicializamos el resultado como 1
    resultado = 1
    # Iteramos desde 1 hasta el número, multiplicando el resultado en cada iteración
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Ejemplo de uso de la función
numero = int(input("Ingrese un número entero no negativo: "))
if numero < 0:
    print("El número ingresado es negativo. Intente nuevamente.")
else:
    print(f"El factorial de {numero} es {factorial(numero)}")
