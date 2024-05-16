class EntityValidationException(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "Entity validation failed."
        super().__init__(message)
