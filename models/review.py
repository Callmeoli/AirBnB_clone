from models.base_model import BaseModel


class Review(BaseModel):
    """ a class User that inherits from BaseModel """

    place_id = ""
    user_id = ""
    text = ""
