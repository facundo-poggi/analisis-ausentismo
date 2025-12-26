def leer_archivo():
    data_abierta = open("turnos.csv", "r", encoding="utf-8")
    data = data_abierta.readlines()
    return data[1:]

def contador_estados(data):
    asistencias = 0
    ausencias = 0
    cancelaciones = 0

    for linea in data:
        linea_limpia = linea.strip()
        partes = linea_limpia.split(",")
        if len(partes) < 4:
            continue

        estado = partes[3].strip()

        if estado == "asistió":
            asistencias += 1

        elif estado == "ausente":
            ausencias += 1

        elif estado == "canceló":
            cancelaciones += 1

    return asistencias, ausencias, cancelaciones

data = leer_archivo()

asistencias, ausencias, cancelaciones = contador_estados(data)

print("Asistencias:", asistencias)
print("Ausencias:" , ausencias)
print("Cancelaciones:", cancelaciones)

total = asistencias + ausencias + cancelaciones
porc_asistencias = round((asistencias/total) * 100, 2)
porc_ausencias = round((ausencias/total) * 100, 2)
porc_cancelaciones = round((cancelaciones/total) * 100, 2)

print("Porcentaje de asistencias:", porc_asistencias)
print("Porcentaje de ausencias:", porc_ausencias)
print("Porcentaje de cancelaciones", porc_cancelaciones)

with open("reporte_ausentismo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("REPORTE DE AUSENTISMO\n")
    archivo.write("----------------------\n")
    archivo.write(f"Asistencias: {asistencias} ({porc_asistencias}%)\n")
    archivo.write(f"Ausencias: {ausencias} ({porc_ausencias}%)\n")
    archivo.write(f"Cancelaciones: {cancelaciones} ({porc_cancelaciones}%)\n")
