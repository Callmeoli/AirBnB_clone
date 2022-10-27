import cmd
import sys
from models.base_model import BaseModel
import shlex
from models import storage


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
        """  Creates a new instance of BaseModel, saves it (to the JSON file) """
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

            key = "{}.{}".format((shlex.split(arg))[0], ((shlex.split(arg))[1]))
            obj = storage.all()
            for k, v in obj.items():
                if key == k:
                    print(v)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
