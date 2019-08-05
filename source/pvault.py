# CLI Parser
import sys
from command_handler import command_handler, get_commands
from db import db_exists, create_db

def help_message():
    message = """usage: pvault [command] [options]

Python CLI based password manager
Generate, store & retrieve your passwords easily & efficiently.

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  generate    generates a random password to your clipboard
              [account name] sets a unique identifier for your password and save; overwrites if exists
              [account name] [password] saves your password given your custom password
  account     shows all saved passwords
              [account name] shows the password of a particular user only
  reset       reset all passwords in the database
  delete      delete all passwords in the database
              [account name] delete only this user in the database"""

    return message

def error_message(command):
    message = """Unknown option: {}
usage: pvault [command] [options]
Try `pvault -h' for more information.""".format(command)

    return message

# PVault Version Number
__version__ = "0.3.0"

if __name__ == "__main__":
    # If the script was ran directly
    if len(sys.argv) <= 1:
        print(help_message())

    # help message
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(help_message())

    # version message
    elif sys.argv[1] == "--version":
        print("PVault", __version__)

    else:
        if not db_exists():
            create_db()

        command = sys.argv[1]

        # command list
        commands = get_commands()
        if command in commands:
            command_handler(command, sys.argv[2:])
        else:
            print(error_message(command))
