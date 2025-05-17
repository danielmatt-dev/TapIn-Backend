class NotificacionException(Exception):
    pass

class NotificacionNotFound(NotificacionException):
    pass

class InvalidNotificacionType(NotificacionException):
    pass

class DisabledNotificacion(NotificacionException):
    pass

class PhoneNotFound(NotificacionException):
    pass
