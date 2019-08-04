# Database Handler
from getpass import getpass
from platform import system
from crypt import hash_pass, encrypt_pass, decrypt_pass, encryptDB, decryptDB
import sqlite3
import os

__dbPath__ = ""

def detect_path():
    # Detect OS so we know where to store DB file
    if "Windows" == system():
        path = __dbPath__ + os.path.join(os.getenv("APPDATA"), "pvault.db")
    elif "Linux" == system():
        path = __dbPath__ + os.path.join(os.getenv("APPDATA"), "pvault.db")
    else:
        path = "pvault.db"

    return path

def db_exists():
    return os.path.exists(detect_path() + ".aes")

def create_db():
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

    encryptDB(path, master_pass)

def check_master(master):
    path = detect_path()
    if decryptDB(path, master, inplace=False):
        os.remove(path)
        return True
    return False

def add_password(master, account, password):
    path = detect_path()
    decryptDB(path, master)

    # Encrypt pass
    password = encrypt_pass(password, master)

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM passwords WHERE account=?", (account,))
        if c.fetchone():
            confirm = input("The password already exists; Do you wish to overwrite it (y/n)? ")
            if confirm.lower() == "n":
                encryptDB(path, master)
                return False
        cmd = """INSERT INTO passwords(account, password)
                VALUES (?, ?)"""
        c.execute(cmd, (account, password))
    encryptDB(path, master)
    return True

def get_password(account, master):
    path = detect_path()

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM passwords WHERE account=?", (account))
        password = c.fetchone()


    # Decrypt pass
    password = decrypt_pass(password, master)

    return password

def get_passwords(account, master):
    path = detect_path()

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM passwords")
        passwords = [item[1] for item in c.fetchall()][1:]


    # Decrypt passwords
    for _ in range(len(passwords)):
        passwords[_] = decrypt_pass(passwords[_], master)

    return passwords
