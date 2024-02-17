class DatabaseError(Exception):
    """Database Error"""
    pass

class CredentialsError(DatabaseError):
    pass