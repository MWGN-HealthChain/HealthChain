from flask import Blueprint, request, jsonify, current_app
from ..service import PatientService
from ..exceptions import BadRequestError

patient_bp = Blueprint("patient", __name__, url_prefix="/api/patients")
patient_service = PatientService()

@patient_bp.route("/", methods=["POST"])
def create_patient():
    try:
        data = request.get_json()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        phone_number = data.get("phone_number")
        date_of_birth = data.get("date_of_birth")

        if not first_name or not last_name:
            raise BadRequestError("first_name and last_name are required")

        patient = patient_service.create_patient(
            first_name, last_name, email, phone_number, date_of_birth
        )

        return jsonify({
            "id": patient.id,
            "first_name": patient.first_name,
            "last_name": patient.last_name,
            "email": patient.email
        }), 201
    except BadRequestError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.exception(e)
        return jsonify({"error": "internal error"}), 500


@patient_bp.route("/login", methods=["POST"])
def login_patient():
    try:
        data = request.get_json()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        patient_id = data.get("patient_id")

        patient = patient_service.login_patient(first_name, last_name, patient_id)
        if not patient:
            return jsonify({"error": "invalid credentials"}), 401

        return jsonify({
            "id": patient.id,
            "first_name": patient.first_name,
            "last_name": patient.last_name
        })
    except Exception as e:
        current_app.logger.exception(e)
        return jsonify({"error": "internal error"}), 500
