# Command Handler
from clipboard import copy_text
from generator import generate_password
from db import check_master, add_password, get_passwords, resetDB, delete_profile
from getpass import getpass
from crypt import hash_pass

def generate(args):
    # handles generation of passwords
    if len(args) >= 1:
        # If we have more arguments then we are dealing with the db here
        # request and verify the master password before proceeding
        master = hash_pass(getpass("Enter master password to generate password: "))
        if not check_master(master):
            print("Incorrect master password")
            return
        password = None
        if len(args) >= 2:
            # A password was specified so use that
            password = args[1]
        else:
            # generate a new password because none was specified
            password = generate_password()
        account = args[0]
        success = add_password(master, account, password)
        if success:
            copy_text(password)
            print("Newly saved password copied to clipboard!")
        else:
            print("Cancelled Operation!")
    else:
        # Just generate a random password
        copy_text(generate_password())
        print("Newly generated password copied to clipboard!")

def account(args):
    # handles getting of password from database
    # request and verify the master password before proceeding
    master = hash_pass(getpass("Enter master password to get account password: "))
    if not check_master(master):
        print("Incorrect master password")
        return
    account = None
    if len(args) != 0:
        # an account was specified to retrieve so use that
        account = args[0]
    get_passwords(master, account)

def reset(args):
    # handles resetting of all passwords in the database
    # request and verify the master password before proceeding
    master = hash_pass(getpass("Enter master password to reset account password: "))
    if not check_master(master):
        print("Incorrect master password")
        return
    # ask for confirmation before proceeding
    confirm = input("Are you sure you want to reset all password in the database (y/n)? ")
    if confirm.lower() in ["y", "yes"]:
        resetDB(master)
        print("Completely reset password database")
    else:
        print("Cancelled Operation!")

def delete(args):
    # handles the removing of password profiles from the database
    # request and verify the master password before proceeding
    master = hash_pass(getpass("Enter master password to delete account password: "))
    if not check_master(master):
        print("Incorrect master password")
        return

    r = True
    if len(args) == 0:
        # if no account was specified, remove all
        confirm = input("Are you sure you want to delete all password in the database (y/n)? ")
        # confirm first incase it was a mistake
        if confirm.lower() in ["y", "yes"]:
            delete_profile(master)
            print("Completely deleted password database")
            r = False
        else:
            r = True
    else:
        confirm = input("Are you sure you want to delete the user password in the database (y/n)? ")
        if confirm.lower() in ["y", "yes"]:
            delete_profile(master, args[0])
            print("Completely deleted user password in the database")
            r = False
        else:
            r = True

    if r:
        print("Cancelled Operation!")

def get_commands():
    # all available commands
    return {"generate": generate, "account": account, "reset": reset, "delete": delete}

def command_handler(command, args):
     commands = get_commands()

     curr_action = commands[command]
     curr_action(args)
