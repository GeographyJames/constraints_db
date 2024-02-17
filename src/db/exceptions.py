class DatabaseError(Exception):
    pass

class CredentialsError(DatabaseError):
    pass