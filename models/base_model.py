import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        if kwargs != {}:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        # Create a shallow copy so that the original dict isn't modified
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict

# Test the BaseModel class
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)

    my_model.save()
    print(my_model)

    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print(f"\t{key}: ({type(my_model_json[key])}) - {my_model_json[key]}")
