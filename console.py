#!/usr/bin/python3
""""Uses Cmd module"""
import cmd
from models .base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    """Class HBNB"""
    prompt = "(hbnb)"
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ End of file marker"""
        return True

    def emptyline(self):
        """Empty commad"""
        pass

    def do_create(self, line):
        """ creates class instance """
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(line) is None:
            print("** class doesn't exist **")
        else:
            base = BaseModel()
            base.save()
            print(base.id)

    def do_show(self, line):
        """show instance"""
        a = []
        for m in line.split(" "):
            a.append(m)
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(a[0]) is None:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        elif a[0]+"."+a[1] not in storage.all():
            print("** no instance found **")
        else:
            print(a[0]+"."+a[1])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        a = []
        for m in line.split(" "):
            a.append(m)
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(a[0]) is None:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id missing **")
        elif a[0] + "." + a[1] not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[a[0] + "." + a[1]]
            storage.save()
    def do_all(self, line):
        """  Prints all string representation of all instances based or not on the class name """
        if len(line) == 0:
            print("** class name missing **")
        elif globals().get(line) is None:
            print("** class doesn't exist **")
        else:
            for k in storage.all():
                print(f'["{storage.all()[k]}"]')



if __name__ == '__main__':
    HBNBCommand().cmdloop()