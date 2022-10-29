import cmd
import sys
from models.base_model import BaseModel
import shlex
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter: """

    classes = {
        "BaseModel": BaseModel
    }

    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self):
        """Quit in the end of file"""
        sys.exit()

    def do_create(self, arg):
        """  Creates a new instance of BaseModel,\
         saves it (to the JSON file) """
        if not arg:
            print("** class name missing **")
        elif arg in self.classes:
            cls = self.classes[arg]
            ins = cls()
            ins.save()
            print(ins.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """  Prints the string representation """
        if not arg:
            print("** class name missing **")
        elif len(shlex.split(arg)) == 1:
            print("** instance id missing **")
        elif not ((shlex.split(arg))[0] in self.classes):
            print("** class doesn't exist **")
        else:

            key = "{}.{}" \
                .format((shlex.split(arg))[0], ((shlex.split(arg))[1]))
            obj_s = storage.all()
            for k, v in obj_s.items():
                if key == k:
                    print(v)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id """

        if not arg:
            print("** class name missing **")
        elif len(shlex.split(arg)) == 1:
            print("** instance id missing **")
        elif not (shlex.split(arg))[0] in self.classes:
            print("** class doesn't exist **")
        else:
            key = "{}.{}" \
                .format((shlex.split(arg))[0], ((shlex.split(arg))[1]))
            obj = storage.all()
            if not (key in obj.keys()):
                print("** no instance found **")
                return
            del obj[key]
            storage.save()

    def do_all(self, arg):
        to_list = []
        if len(shlex.split(arg)) == 1 and \
                (shlex.split(arg))[0] in self.classes:
            obj_l = storage.all()
            for k, v in obj_l.items():
                to_list.append(str(obj_l[k]))
            print(to_list)
        elif len(shlex.split(arg)) == 0:
            obj_l = storage.all()
            for k, v in obj_l.items():
                to_list.append(str(obj_l[k]))
            print(to_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        if len(shlex.split(arg)) == 0:
            print("** class name missing **")
        elif len(shlex.split(arg)) == 1:
            if not (shlex.split(arg))[0] in self.classes:
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
        elif len(shlex.split(arg)) == 2:
            if not (shlex.split(arg))[0] in self.classes:
                print("** class doesn't exist **")
                return
            key = "{}.{}" \
                .format((shlex.split(arg))[0], ((shlex.split(arg))[1]))
            obj_u = storage.all()
            if not (key in obj_u.keys()):
                print("** no instance found **")
                return
        elif len(shlex.split(arg)) == 3:
            if not (shlex.split(arg))[0] in self.classes:
                print("** class doesn't exist **")
                return
            key = "{}.{}" \
                .format((shlex.split(arg))[0], ((shlex.split(arg))[1]))
            obj_u = storage.all()
            if not (key in obj_u.keys()):
                print("** no instance found **")
                return
            if not (shlex.split(arg))[2] in obj_u[key].keys():
                print("** attribute name missing **")
                return
            print("** value missing **")
        elif len(shlex.split(arg)) == 4:
            if not (shlex.split(arg))[0] in self.classes:
                print("** class doesn't exist **")
                return
            key = "{}.{}" \
                .format((shlex.split(arg))[0], ((shlex.split(arg))[1]))
            obj_u = storage.all()
            if not (key in obj_u.keys()):
                print("** no instance found **")
                return

            if not (hasattr(obj_u[key], shlex.split(arg)[2])):
                print("** attribute name missing **")
            else:
                setattr(obj_u[key], (shlex.split(arg))[2], (shlex.split(arg))[3])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
