from flask import Blueprint, request, jsonify
from model.usuarios_model import Usuarios
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

user_bp = Blueprint("usuarios", __name__)


@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email=data.get("email")
    password = data.get("password")
    roles = data.get("roles")

    if not name or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400

    existing_user = Usuarios.find_by_name(name)
    if existing_user:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400

    new_user = Usuarios(name, password, roles)
    new_user.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    name = data.get("name")
    password = data.get("password")

    usuario = Usuarios.find_by_name(name)
    if usuario and check_password_hash(usuario.password_hash, password):
        access_token = create_access_token(
            identity={"name": name, "roles": usuario.roles}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
