import csv

def leer_turnos_desde_csv(ruta_archivo):
    turnos =[]
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            turno = {
                "fecha" : fila["fecha"],
                "hora" : fila["hora"],
                "paciente" : fila["paciente"],
                "estado" : fila["estado"].lower().strip() 
            }
            turnos.append(turno)
    return turnos

turnos = leer_turnos_desde_csv("turnos.csv")
print("Total de turnos:", len(turnos))
print("Primer turno:", turnos[0])

ausentes = [t for t in turnos if t["estado"] == "ausente"]
asistidos =[t for t in turnos if t["estado"] == "asistió"]
cancelados =[t for t in turnos if t["estado"] == "canceló"]

print("Total de ausentes:", len(ausentes))
print("Total de asistidos:", len(asistidos))
print("Total de cancelados:", len(cancelados))

porcentaje_ausentismo = round((len(ausentes) / len(turnos)) * 100,2)
print("Porcentaje de ausentismo;", porcentaje_ausentismo, "%")

