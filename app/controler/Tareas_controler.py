from flask import Blueprint, request, jsonify
from model.Tareas_model import Tareas
from view.tareas_view import render_Tarea_list, render_Tarea_detail
from utils.decoradores import jwt_required, roles_required

tarea_bp = Blueprint("tarea", __name__)

@tarea_bp.route("/taks", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_Tareas():
    Tareas = Tareas.get_all()
    return jsonify(render_Tarea_list(Tareas))

@tarea_bp.route("/taks/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_animal(id):
    tarea = Tareas.get_by_id(id)
    if tarea:
        return jsonify(render_Tarea_detail(tarea))
    return jsonify({"error": "Tarea no encontrado"}), 404

@tarea_bp.route("/taks", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_tarea():
    data = request.json
    title = data.get("title")
    description=data.get("description")
    status=data.get("status")
    created_st=data.get("created_at")
    assigned_to=data.get("assigned_to")
    

    if not title or not description or status or created_st or assigned_to is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    tarea =Tareas(title=title , description=description, status=status,created_st=created_st, assigned_to=assigned_to)
    tarea.save()

    return jsonify(render_Tarea_detail(tarea)), 201


@tarea_bp.route("/taks/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_tareas(id):
    tarea = Tareas.get_by_id(id)

    if not tarea:
        return jsonify({"error": "Tareas no encontrado"}), 404

    data = request.json
    title = data.get("title")
    description=data.get("description")
    status=data.get("status")
    created_st=data.get("created_at")
    assigned_to=data.get("assigned_to")
    

    tarea.update(title=title , description=description, status=status,created_st=created_st, assigned_to=assigned_to)

    return jsonify(render_Tarea_detail(tarea))

@tarea_bp.route("/taks/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_tarea(id):
    tarea = Tareas.get_by_id(id)

    if not tarea:
        return jsonify({"error": "Tarea no encontrado"}), 404

    tarea.delete()

    return "", 204
