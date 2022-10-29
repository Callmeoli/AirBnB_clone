#!/usr/bin/python3
""" Init module for base model """


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()