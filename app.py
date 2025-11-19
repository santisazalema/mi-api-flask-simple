# app.py
from flask import Flask, jsonify, request

# 1. Inicializa la aplicación Flask
app = Flask(__name__)

# 2. Datos de prueba (simulan una base de datos de "tareas")
tareas = [
    {'id': 1, 'titulo': 'Aprender Flask', 'completada': False},
    {'id': 2, 'titulo': 'Subir API a GitHub', 'completada': False}
]

# --- Rutas de la API (Endpoints) ---

# Ruta 1: Obtener todas las tareas (Método GET)
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    # Devuelve el diccionario 'tareas' convertido a JSON
    return jsonify({'tareas': tareas})

# Ruta 2: Crear una nueva tarea (Método POST)
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    # Obtiene los datos JSON que envía el cliente
    if not request.json or 'titulo' not in request.json:
        return jsonify({'error': 'Falta el título'}), 400

    nueva_tarea = {
        'id': tareas[-1]['id'] + 1 if tareas else 1, # Asigna un nuevo ID
        'titulo': request.json['titulo'],
        'completada': False
    }
    tareas.append(nueva_tarea)
    return jsonify({'tarea': nueva_tarea}), 201 # 201 es el código de "Creado"

# 3. Ejecución de la aplicación
if __name__ == '__main__':
    # 'debug=True' permite recargar automáticamente al guardar cambios
    app.run(debug=True)
