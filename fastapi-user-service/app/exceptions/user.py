from app.exceptions.exceptions import AppException

class UserNotFoundException(AppException):
    pass

class UserAlreadyExistsException(AppException):
    pass
