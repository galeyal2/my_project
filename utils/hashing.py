from passlib.context import CryptContext


class Hash():
    pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated='auto')

    @staticmethod
    def bcrypt(password: str):
        return Hash.pwd_cxt.hash(password)


