# Definir la función para generar la serie de Fibonacci hasta un límite dado
def fibonacci_hasta_limite(limite):
    # Inicializar los primeros dos números de la serie
    a, b = 0, 1
    # Lista para almacenar los números de la serie
    serie_fibonacci = []
    
    # Generar la serie de Fibonacci hasta alcanzar el límite dado
    while a <= limite:
        serie_fibonacci.append(a)
        a, b = b, a + b
    
    return serie_fibonacci

# Generar la serie de Fibonacci hasta el número 50
serie_fibonacci_50 = fibonacci_hasta_limite(50)

# Imprimir la serie de Fibonacci
print("Serie de Fibonacci hasta el número 50:")
print(serie_fibonacci_50)
