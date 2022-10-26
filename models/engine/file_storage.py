import json
import os.path


class FileStorage:
    def __int__(self):
        """ Init method for class FileStorage """
        self.__file_path = ""
        self.__objects = {}

    def all(self):
        """ Return the dictionary objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
         with open(self.__file_path, 'w', encoding='utf-8') as fp:
             tojson_dic = {}
             for k ,v in self.__objects.items():
                 dic = self.__objects[k].to_dic()
                 tojson_dic[k] = dic
            fp.write(json.dumps(tojson_dic))


    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.isfile(self.__file_path) is True:
            jason_data = {}
            with open(self.__file_path, 'r', encoding='utf-8') as fp:
                file_data = fp.read()
                jason_data = json.loads(file_data)

            for k, v in jason_data.items():
                self.new(v)