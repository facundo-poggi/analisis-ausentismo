contador_cancelados = 0

for turno in turnos:
    if turno["estado"] == "canceló":
        contador_cancelados += 1

print("Cancelados:", contador_cancelados)

contador_no_asistidos = 0

for turno in turnos:
    if turno["estado"] != "asistió":
        contador_no_asistidos !=1

print("No Asistidos:", contador_no_asistidos)


ausentes = []

for turno in turnos:
    if turno["estado"] == "ausente":
        ausentes.append(turno)

print("Lista de ausentes:", len(ausentes))