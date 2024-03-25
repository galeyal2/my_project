from pydantic import BaseModel


class UserSchema(BaseModel):
    user: str
    email: str
    password: str

    class Config():
        from_attributes = True


class ShowUser(BaseModel):
    id: int
    user: str
    email: str

    class Config():
        from_attributes = True


class UpdateUser(BaseModel):
    id: int
    user: str
    email: str
    password:str

    class Config():
        from_attributes = True