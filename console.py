#!/usr/bin/python3
"""console.py"""
import cmd
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):

    """
    Contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    __classes = ["BaseModel"]

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file)and prints the id.
        """

        if not arg:
            print("** class name missing **")

        elif not arg == "BaseModel":
            print("** class doesn't exist **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except Exception:
                pass

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id
        """
        instances = storage.all()

        arguments = arg.split()
        class_name = arguments[0]
        class_id = arguments[1]

        key = f"{class_name}.{class_id}"

        if len(arguments) < 1:
            print("** class name missing **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        elif not  arguments[0] == "BaseModel":
            print("** class doesn't exist **")
        elif not key in instances:
                print("** no instance found **")
        else:
            print(instances[key])

    def do_destroy(self, arg):
        arguments = arg.split()
        class_name = arguments[0]
        class_id = arguments[1]
        
        instances = storage.all()
        key = f"{class_name}.{class_id}"


        if len(arguments) < 1:
            print("** class name missing **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        elif not  arguments[0] == "BaseModel":
            print("** class doesn't exist **")
        elif not key in instances:
                print("** no instance found **")
        else:
            del instances[key]
            storage.save()
    
    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        arg_parts = arg.split()
        obj_list = []

        if not arg_parts:
            # If no arguments, display all instantiated objects
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            class_name = arg_parts[0]  # Extract the first argument

            if class_name not in HBNBCommand.__classes:
                print(" class doesn't exist ")
            else:

                # Retrieve instances of the specified class
                for obj in storage.all().values():
                    if obj.__class__.__name__ == class_name:
                        obj_list.append(str(obj))
                print(obj_list)

            # Display string representations of instances of the specified class

    def emptyline(self):
        """Empty line + Enter does nothing"""
        pass

    def do_EOF(self, line):
        """Command to exit the program"""
        return True

    def do_quit(self, arg):
        """command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
