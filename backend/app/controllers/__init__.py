from flask import Blueprint

# Import blueprints from each controller
from .patient_controller import patient_bp
# from .credential_controller import credential_bp
from .record_controller import record_bp
from .hospital_controller import register_hospital_routes

def register_controllers(app):
    """
    Register all controller blueprints and routes with the Flask app.
    """
    # Blueprints
    app.register_blueprint(patient_bp)
    # app.register_blueprint(credential_bp)
    app.register_blueprint(record_bp)

    # Hospital routes (since they’re registered via function)
    hospital_bp = Blueprint("hospital", __name__, url_prefix="/api")
    register_hospital_routes(hospital_bp)
    app.register_blueprint(hospital_bp)
