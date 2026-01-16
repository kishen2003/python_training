class AppException(Exception):
    """Base application exception"""
    pass

class DatabaseException(AppException):
    """Raised when a database error occurs"""
    pass
