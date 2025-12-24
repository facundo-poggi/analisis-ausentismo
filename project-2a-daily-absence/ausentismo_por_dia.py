import csv
      
def ausentismo_por_dia(ruta_csv):
    ausencias_diarias = {}

    with open(ruta_csv, "r", encoding= "utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["estado"] == "ausente":  
               if fila["fecha"] in ausencias_diarias:
                   ausencias_diarias[fila["fecha"]] += 1
               else:
                   ausencias_diarias[fila["fecha"]] = 1

    return ausencias_diarias

resultado = ausentismo_por_dia("turnos.csv")

for fecha in sorted(resultado):
    print(fecha, resultado[fecha])
 
         
                                        




