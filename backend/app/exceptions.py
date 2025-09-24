class AppError(Exception):
    """Base class for all custom application errors."""
    status_code = 500
    message = "An unexpected error occurred."

    def __init__(self, message=None, status_code=None):
        super().__init__(message or self.message)
        if status_code:
            self.status_code = status_code


class BadRequestError(AppError):
    """400 - Client sent invalid request data."""
    status_code = 400
    message = "Bad request."


class UnauthorizedError(AppError):
    """401 - User not authorized (invalid/missing credentials)."""
    status_code = 401
    message = "Unauthorized access."


class ForbiddenError(AppError):
    """403 - User does not have permission."""
    status_code = 403
    message = "Forbidden."


class NotFoundError(AppError):
    """404 - Resource not found."""
    status_code = 404
    message = "Resource not found."


class ConflictError(AppError):
    """409 - Resource already exists (e.g., duplicate email)."""
    status_code = 409
    message = "Conflict error."


class ValidationError(AppError):
    """422 - Data validation failed."""
    status_code = 422
    message = "Validation error."
