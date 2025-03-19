import subprocess
import json
import os

# Ruta del archivo JSON dentro de la carpeta "data"
json_path = os.path.join("..", "data", "datos.json") 

# Crear la carpeta "data" si no existe (usando ruta relativa a 'python')
data_path = os.path.join("..", "data")
if not os.path.exists(data_path):
    os.makedirs(data_path)

# Lista para almacenar los datos ingresados por el usuario
personas = []

while True:
    # Pedir datos al usuario
    nombre = input("Ingrese el nombre (o 'finalizar' para salir): ").strip()
    if nombre.lower() in ["finalizar", "terminado"]:
        break

    edad = int(input("Ingrese la edad: "))
    nota = float(input("Ingrese la nota: "))

    # Guardar los datos en la lista
    personas.append([nombre, edad, nota])

# Guardamos los datos en un archivo JSON dentro de "data"
with open(json_path, "w") as archivo:
    json.dump(personas, archivo)

print("\nLista de personas ingresadas en Python:")
for p in personas:
    print(f"Nombre: {p[0]}, Edad: {p[1]}, Nota: {p[2]}")

print("\nEjecutando la parte en JavaScript para ordenar los datos...\n")

js_path = os.path.join("..", "javascript", "programa.js")
subprocess.run(["node", js_path])
