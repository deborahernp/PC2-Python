def obtener_fecha_en_formato_iso(fecha_input):
    meses = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }

    # Dividir la entrada de fecha en partes
    partes = fecha_input.split()

    # Si la entrada de fecha es del formato "mes/día/año"
    if len(partes) == 3:
        mes = partes[0]
        dia = partes[1]
        anio = partes[2]
    # Si la entrada de fecha es del formato "mes día, año"
    elif len(partes) == 3 and ',' in partes[1]:
        mes = partes[0]
        dia = partes[1].replace(',', '')
        anio = partes[2]
    else:
        print("Formato de fecha no válido.")
        return

    # Obtener el mes en formato numérico
    mes_numero = meses.get(mes)
    if mes_numero is None:
        print("Nombre de mes no válido.")
        return

    # Completar con ceros a la izquierda si es necesario
    dia = dia.zfill(2)
    mes_numero = mes_numero.zfill(2)

    # Generar la fecha en formato AAAA-MM-DD
    fecha_iso = f"{anio}-{mes_numero}-{dia}"
    return fecha_iso

# Solicitar al usuario una fecha
fecha_input = input("Ingrese una fecha en formato mes/día/año o mes día, año: ")

# Obtener la fecha en formato ISO
fecha_iso = obtener_fecha_en_formato_iso(fecha_input)

if fecha_iso:
    print("Fecha en formato AAAA-MM-DD:", fecha_iso)
