def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    elif numero <= 3:
        return True  # 2 y 3 son primos
    elif numero % 2 == 0 or numero % 3 == 0:
        return False  # Los múltiplos de 2 y 3 no son primos
    else:
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False  # Si es divisible por algún número entre i e i+2, no es primo
            i += 6
        return True  # Si no fue divisible por ningún número, es primo

# Ejemplo de uso de la función
numero = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")