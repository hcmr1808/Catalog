from src.Domain.Exceptions.EntityValidationException import EntityValidationException

class DomainValidation:

    @staticmethod
    def NotNull(target: str, fieldname: str):
        if target is None:
            raise EntityValidationException(f"{fieldname} should not be null.")
        
    @staticmethod
    def NotNullOrEmpty(target:str, fieldname:str):
        if not target or target.strip() == '':
            raise EntityValidationException(f"{fieldname} should not be empty or null.")
    
    @staticmethod
    def MinLength(target:str, minLength:int, fieldname:str):
        if len(target) < minLength:
            raise EntityValidationException(f"{fieldname} should not be less than {minLength} characters.")
    
    @staticmethod
    def MaxLength(target:str, maxLength:int, fieldname:str):
        if len(target) > maxLength:
            raise EntityValidationException(f"{fieldname} should not be greater than {maxLength} characters.")

