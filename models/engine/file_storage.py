import json


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
             j_dic = {}
             for k ,v in self.__objects.items():
                 dic = self.__objects[k].to_dic()
                 j_dic[k] = dic
            fp.write(json.dumps(j_dic))
