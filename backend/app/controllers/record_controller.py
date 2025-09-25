from flask import Blueprint, request, jsonify, current_app
from ..service import MedicalRecordService
from ..exceptions import BadRequestError

record_bp = Blueprint("record", __name__, url_prefix="/api/records")
record_service = MedicalRecordService()

@record_bp.route("/add", methods=["POST"])
def add_record():
    try:
        data = request.form.to_dict()
        provider_id = data.get("provider_id")
        patient_id = data.get("patient_id")

        if not provider_id or not patient_id:
            raise BadRequestError("provider_id and patient_id are required")

        # Optional file
        f = request.files.get("file")
        file_tuple = (f.read(), f.filename) if f else None

        record = record_service.add_record(provider_id, patient_id, data, file_tuple)

        return jsonify({
            "id": record.id,
            "title": record.title,
            "status": record.status,
            "sui_object_id": record.sui_object_id
        }), 201
    except BadRequestError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.exception(e)
        return jsonify({"error": "internal error"}), 500


@record_bp.route("/patient/<patient_id>", methods=["GET"])
def list_patient_records(patient_id):
    try:
        records = record_service.list_by_patient(patient_id)
        return jsonify([
            {
                "id": r.id,
                "title": r.title,
                "description": r.description,
                "status": r.status,
                "sui_object_id": r.sui_object_id
            } for r in records
        ])
    except Exception as e:
        current_app.logger.exception(e)
        return jsonify({"error": "internal error"}), 500
