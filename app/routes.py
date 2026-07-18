from flask import Blueprint, jsonify, request
from app.models import db, Task

api = Blueprint("api", __name__)

@api.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API de tareas funcionando correctamente",
        "rutas": [
            "/tareas",
            "/tareas/<id>"
        ]
    }), 200


@api.route("/tareas", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200


@api.route("/tareas/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(task.to_dict()), 200


@api.route("/tareas", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes enviar datos JSON"}), 400

    if "titulo" not in data or not str(data["titulo"]).strip():
        return jsonify({"error": "El campo 'titulo' es obligatorio"}), 400

    task = Task(
        titulo=str(data["titulo"]).strip(),
        completada=bool(data.get("completada", False))
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201


@api.route("/tareas/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes enviar datos JSON"}), 400

    if "titulo" in data:
        if not str(data["titulo"]).strip():
            return jsonify({"error": "El campo 'titulo' no puede estar vacío"}), 400
        task.titulo = str(data["titulo"]).strip()

    if "completada" in data:
        task.completada = bool(data["completada"])

    db.session.commit()
    return jsonify(task.to_dict()), 200


@api.route("/tareas/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Tarea eliminada correctamente"}), 200