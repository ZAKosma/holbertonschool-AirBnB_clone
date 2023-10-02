#!/usr/bin/python3
"""My File Storage class"""
import json
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as objFile:
            temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(temp, objFile)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as objFile:
                temp = json.load(objFile)
                for k, v in temp.itemps():
                    restoredObject = eval(v['__class__'])(**v)
                    FileStorage.__objects[k] = restoredObject
        except FileNotFoundError:
            pass