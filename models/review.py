#!/usr/bin/python3
""" Review Mod"""

from models.base_model import BaseModel

class Review(BaseModel):
    """CLasd Review """
    place_id = ""
    user_id = ""
    text = ""