# Función para ingresar las calificaciones de un alumno
def ingresar_calificaciones():
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    return {'Alumno': nombre, 'Notas': [nota1, nota2, nota3]}

# Función para mostrar el listado de alumnos
def mostrar_listado(alumnos):
    print("Listado de Alumnos:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")

# Inicializar la lista de alumnos
alumnos = []

# Pedir al usuario la cantidad de alumnos a ingresar
num_alumnos = int(input("Ingrese la cantidad de alumnos a registrar: "))

# Ingresar los datos de cada alumno
for _ in range(num_alumnos):
    alumno = ingresar_calificaciones()
    alumnos.append(alumno)

# Mostrar el listado completo de alumnos
mostrar_listado(alumnos)