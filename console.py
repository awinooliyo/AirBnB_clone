#!/usr/bin/python3
"""console.py"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "

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
