class AppError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


def register_error_handlers(app):
    @app.errorhandler(AppError)
    def handle_app_error(error: AppError):
        return {"error": error.message}, error.status_code

    @app.errorhandler(404)
    def handle_not_found(_):
        return {"error": "Not Found"}, 404

    @app.errorhandler(500)
    def handle_internal_error(_):
        return {"error": "Internal Server Error"}, 500