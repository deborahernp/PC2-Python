def contar_digitos(numero, digito):
    # Convertir el número a cadena para poder utilizar el método count()
    numero_str = str(numero)
    # Contar la cantidad de veces que aparece el dígito en el número
    cantidad = numero_str.count(str(digito))
    return cantidad

# Ejemplo de uso de la función
numero = 15789000
digito = 0
cantidad = contar_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número {numero}: {cantidad}")