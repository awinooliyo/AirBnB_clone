#!/usr/bin/python3
"""Module defines class HBNCommand"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):

    """
    Contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            }

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file)and prints the id.
        """

        if not arg:
            print("** class name missing **")

        elif arg not in HBNBCommand.__classes:
            print("** class doesn\'t exist **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except Exception:
                pass

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        instances = storage.all()

        arguments = arg.split()

        if len(arguments) < 1:
            print("** class name missing **")
            return
        else:
            class_name = arguments[0]

        if len(arguments) < 2:
            print("** instance id missing **")
            return
        else:
            class_id = arguments[1]

        key = "{}.{}".format(class_name, class_id)

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif key not in instances:
            print("** no instance found **")
            return
        else:
            print(instances[key])

    def do_destroy(self, arg):

        instances = storage.all()

        if arg:
            arguments = arg.split()

            if len(arguments) == 2:
                class_name = arguments[0]
                class_id = arguments[1]
                key = f"{class_name}.{class_id}"

                if arguments[0] not in HBNBCommand.__classes:
                    print("** class doesn\'t exist **")
                elif key not in instances:
                    print("** no instance found **")
                else:
                    del instances[key]
                    storage.save()
            else:
                print("** instance id missing **")

        else:
            print("** class name missing **")

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

            # Check for quoted string argument with spaces
            if class_name.startswith('"') and class_name.endswith('"'):
                class_name = class_name[1:-1]  # Remove quotes

            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist ** ")
            else:

                # Retrieve instances of the specified class
                for obj in storage.all().values():
                    if obj.__class__.__name__ == class_name:
                        obj_str = str(obj)

                        obj_str = obj_str.replace('"', "'")
                        obj_list.append(obj_str)
                print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        arguments = arg.split()

        if not arguments:
            print("** class name missing **")
            return

        class_name = arguments[0]

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments[1]

        if len(arguments) < 3:
            print("** attribute name missing **")
            return

        attr_name = arguments[2]

        if len(arguments) < 4:
            print("** value missing **")
            return

        attr_value = arguments[3]

        if not all((class_name, instance_id, attr_name, attr_value)):
            print("** attribute name missing **")
            return

        key = class_name + "." + instance_id
        if key not in storage.all():  # Assuming storage has objects
            print("** class doesn't exist **")
            return

        obj = storage.all()[key]

        if attr_name in ["id", "created_at", "updated_at"]:
            print("** cannot update id, created_at, or updated_at **")
            return

        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            if attr_value is not None:
                if attr_type == str and attr_value.startswith('"') \
                        and attr_value.endswith('"'):
                    attr_value = attr_value[1:-1]
                try:
                    cast_value = attr_type(attr_value)
                except ValueError:
                    print(f" invalid value for {attr_name} ")
                    return
                if isinstance(cast_value, (str, int, float)):
                    setattr(obj, attr_name, cast_value)
                    obj.save()
                    storage.save()
                else:
                    print("Attribute type must be string, int, or float")
            else:
                print(" value missing ")
        else:
            # Dynamically adding the attribute if it doesn't exist
            setattr(obj, attr_name, attr_value)
            obj.save()
            storage.save()

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
