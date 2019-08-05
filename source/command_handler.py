# Command Handler
from clipboard import copy_text
from generator import generate_password
from db import check_master, add_password, get_passwords
from getpass import getpass
from crypt import hash_pass

def generate(args):
    if len(args) >= 1:
        master = hash_pass(getpass("Enter master password to generate password: "))
        if not check_master(master):
            print("Incorrect master password")
            return
        password = None
        if len(args) >= 2:
            password = args[1]
        else:
            password = generate_password()
        account = args[0]
        success = add_password(master, account, password)
        if success:
            copy_text(password)
            print("Newly saved password copied to clipboard!")
        else:
            print("Cancelled Operation!")
    else:
        copy_text(generate_password())
        print("Newly generated password copied to clipboard!")

def account(args):
    master = hash_pass(getpass("Enter master password to get account password: "))
    if not check_master(master):
        print("Incorrect master password")
        return
    account = None
    if len(args) != 0:
        account = args[0]
    get_passwords(master, account)

def get_commands():
    return {"generate": generate, "account": account}

def command_handler(command, args):
     commands = get_commands()

     curr_action = commands[command]
     curr_action(args)
