from flask import request, jsonify, current_app
from ..service import HospitalService
from ..exceptions import BadRequestError

hospital_service = HospitalService()

def register_hospital_routes(bp):
    # -----------------------
    # Hospital registration
    # -----------------------
    @bp.route("/hospital/register", methods=["POST"])
    def register_hospital():
        try:
            data = request.get_json()
            facility_name = data.get("facility_name")
            license_number = data.get("license_number")
            address = data.get("address")

            if not facility_name or not license_number:
                raise BadRequestError("facility_name and license_number are required")

            hospital = hospital_service.register_hospital(
                facility_name, license_number, address
            )

            return jsonify({
                "id": hospital.id,
                "facility_name": hospital.facility_name,
                "is_verified": hospital.is_verified
            }), 201

        except BadRequestError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            current_app.logger.exception(e)
            return jsonify({"error": "internal error"}), 500

    # -----------------------
    # Hospital login
    # -----------------------
    @bp.route("/hospital/login", methods=["POST"])
    def login_hospital():
        try:
            data = request.get_json()
            license_number = data.get("license_number")

            hospital = hospital_service.login_hospital(license_number)
            if not hospital:
                return jsonify({"error": "invalid license number"}), 401

            return jsonify({
                "id": hospital.id,
                "facility_name": hospital.facility_name,
                "is_verified": hospital.is_verified
            })
        except Exception as e:
            current_app.logger.exception(e)
            return jsonify({"error": "internal error"}), 500
