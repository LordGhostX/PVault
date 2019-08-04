# CLI Parser
import sys

def help_message():
    message = """usage: pvault [command] [options]

Python CLI based password manager
Generate, store & retrieve your passwords easily & efficiently.

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit"""

    return message

def error_message(command):
    message = """Unknown option: {}
usage: pvault [command] [options]
Try `pvault -h' for more information.""".format(command)

    return message

if __name__ == "__main__":
    # PVault Version Number
    version_number = "0.0.1"

    # If the script was ran directly
    if len(sys.argv) <= 1:
        print(help_message())

    # help message
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(help_message())

    # version message
    elif sys.argv[1] == "--version":
        print("PVault", version_number)

    else:
        command = sys.argv[1]
        print(error_message(command))
