def omitir_vocales(cadena):
    # Definir las vocales en mayúsculas y minúsculas
    vocales = "AEIOUaeiou"
    # Inicializar una cadena vacía para almacenar el resultado
    resultado = ""
    # Iterar sobre cada carácter en la cadena
    for caracter in cadena:
        # Verificar si el carácter no es una vocal
        if caracter not in vocales:
            # Agregar el carácter al resultado
            resultado += caracter
    return resultado

# Solicitar al usuario una cadena de texto
texto = input("Ingrese una cadena de texto: ")
# Obtener la cadena con las vocales omitidas
resultado = omitir_vocales(texto)
# Imprimir el resultado
print("Texto con vocales omitidas:", resultado)
