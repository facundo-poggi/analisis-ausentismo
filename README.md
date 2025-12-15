# Análisis de Ausentismo en Turnos de Salud

## Descripción
Proyecto de análisis descriptivo de ausentismo a partir de registros de turnos de un centro de salud.  
El objetivo es identificar niveles de ausentismo y obtener métricas básicas que ayuden a comprender el comportamiento de los turnos.

Este proyecto forma parte de un portfolio de aprendizaje en Python y análisis de datos.

---

## Datos
El análisis se realiza sobre un archivo CSV (`turnos.csv`) que contiene información de turnos con los siguientes campos:

- fecha  
- hora  
- paciente  
- estado (asistió / ausente / canceló)

---

## Funcionalidades
El proyecto permite:

- Contar turnos cancelados
- Contar turnos no asistidos (ausentes + cancelados)
- Filtrar turnos ausentes
- Calcular cantidad de ausentes
- Listar pacientes ausentes

---

## Estructura del proyecto
- `analisis.py`: análisis y métricas de ausentismo  
- `panel_ausentismo.py`: procesamiento y visualización por consola  
- `turnos.csv`: datos de entrada  
- `reporte_ausentismo.txt`: reporte generado  
- `practica.py`: archivo de práctica  

---

## Tecnologías utilizadas
- Python 3
- Git / GitHub
- CSV (manejo de archivos)

---

## Cómo ejecutar el proyecto
1. Clonar el repositorio
2. Ejecutar el script principal desde la terminal:

```bash
python panel_ausentismo.py
