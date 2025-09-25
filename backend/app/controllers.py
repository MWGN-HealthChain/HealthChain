from flask import Blueprint, request, current_app, jsonify
from .services import CredentialService
from .exceptions import BadRequestError

def register_blueprints(app):
    bp = Blueprint("api", __name__, url_prefix="/api")
    service = CredentialService()

    @bp.route("/credentials/issue", methods=["POST"])
    def issue():
        # Expect multipart form: provider_id, patient_id, title, description, file
        try:
            provider_id = request.form["provider_id"]
            patient_id = request.form["patient_id"]
            title = request.form.get("title", "")
            description = request.form.get("description", "")
            f = request.files.get("file")
            if not f:
                raise BadRequestError("file is required")
            file_bytes = f.read()
            filename = f.filename
            cred = service.issue_credential(provider_id, patient_id, title, description, file_bytes, filename)
            return jsonify({"id": cred.id, "sui_object_id": cred.sui_object_id}), 201
        except BadRequestError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            current_app.logger.exception(e)
            return jsonify({"error": "internal error"}), 500

    @bp.route("/credentials/<id>", methods=["GET"])
    def get_cred(id):
        try:
            cred = service.get_credential(id)
            return jsonify({
                "id": cred.id,
                "title": cred.title,
                "description": cred.description,
                "walrus_blob_id": cred.walrus_blob_id,
                "sui_object_id": cred.sui_object_id,
                "status": cred.status
            })
        except Exception as e:
            current_app.logger.exception(e)
            return jsonify({"error": "not found"}), 404

    app.register_blueprint(bp)
