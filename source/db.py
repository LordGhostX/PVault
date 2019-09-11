# Database Handler
from getpass import getpass
from platform import system
from clipboard import copy_text
from crypt import hash_pass, encrypt_pass, decrypt_pass, encryptDB, decryptDB
from generator import generate_password
import sqlite3
import os

__dbPath__ = "pvault.db" # Password Database Name

def detect_path():
    # Detect OS so we know where to store DB file
    # Supports Windows, Linux, MAC
    if system() in ["Windows", "Linux", "Darwin"]:
        path = os.path.join(os.path.expanduser("~"), __dbPath__)
    else:
        path = __dbPath__

    return path

def db_exists():
    # Checks if the password database exists
    return os.path.exists(detect_path() + ".aes")

def create_db():
    # Creates our password database initiating it with our master password
    path = detect_path()

    # Create and hash the master password
    while True:
        master_pass = getpass("Set a master password: ")
        master_pass_2 = getpass("Enter master password again: ")
        if master_pass == master_pass_2:
            del master_pass_2
            break
        print("The passwords don't match!\n")
    master_pass = hash_pass(master_pass)

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        cmd = """CREATE TABLE IF NOT EXISTS passwords (
                    id integer PRIMARY KEY,
                    account text NOT NULL,
                    password text NOT NULL);"""
        c.execute(cmd)
    conn.close()
    encryptDB(path, master_pass)

def check_master(master):
    # Check if a given master password is valid or not
    path = detect_path()
    if decryptDB(path, master, inplace=False):
        os.remove(path)
        return True
    return False

def add_password(master, account, password):
    # Adds a new password profile to the database
    path = detect_path()
    decryptDB(path, master)

    # Encrypt pass
    password = encrypt_pass(password, master)

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM passwords WHERE account=?", (account,))
        r = True
        if c.fetchone():
            # the account already exists; so replace it
            confirm = input("The password already exists; Do you wish to overwrite it (y/n)? ")
            r = False
            if confirm.lower() in ["y", "yes"]:
                cmd = """UPDATE passwords
                         SET password = ?
                         WHERE account = ?"""
                c.execute(cmd, (password, account))
        if r:
            cmd = """INSERT INTO passwords(account, password)
                    VALUES (?, ?)"""
            c.execute(cmd, (account, password))
    conn.close()
    encryptDB(path, master)
    return True

def get_passwords(master, account):
    # Get passwords from the database
    path = detect_path()
    decryptDB(path, master)

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        if account:
            c.execute("SELECT * FROM passwords WHERE account=?", (account,))
            password = c.fetchone()
            if password:
                copy_text(decrypt_pass(password[2], master))
                print("Password has been copied to your clipboard!")
            else:
                print("The specified account does not exist!")
        else:
            c.execute("SELECT * FROM passwords")
            passwords = c.fetchall()
            for password in passwords:
                print("{} = {}".format(password[1], decrypt_pass(password[2], master)))
    conn.close()
    encryptDB(path, master)

def resetDB(master):
    # Reset all the passwords in the database
    path = detect_path()
    decryptDB(path, master)

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM passwords")
        passwords = c.fetchall()
        for password in passwords:
            new_pass = encrypt_pass(generate_password(), master)
            cmd = """UPDATE passwords
                     SET password = ?
                     WHERE id = ?"""
            c.execute(cmd, (new_pass, password[0]))

    conn.close()
    encryptDB(path, master)

def delete_profile(master, account=None):
    # Delete a password profile from the database
    path = detect_path()
    decryptDB(path, master)

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        if account:
            cmd = "DELETE FROM passwords WHERE account = ?"
            c.execute(cmd, (account,))
        else:
            cmd = "DELETE FROM passwords"
            c.execute(cmd)
    conn.close()
    encryptDB(path, master)
