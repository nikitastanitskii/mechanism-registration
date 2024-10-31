import bcrypt


class HashPassword:
    @staticmethod
    def hash(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
