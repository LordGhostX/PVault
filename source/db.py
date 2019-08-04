# Database Handler
from getpass import getpass
from platform import system
from crypt import hash_pass, encrypt_pass, decrypt_pass
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
    return os.path.exists(detect_path())

def create_db():
    path = detect_path()

    # Create and hash the master password
    master_pass = getpass("Set a master password: ")
    master_pass = hash_pass(master_pass)

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        cmd = """CREATE TABLE IF NOT EXISTS passwords (
                    id integer PRIMARY KEY,
                    account text NOT NULL,
                    password text NOT NULL,
                    group text
                );"""
        c.execute(cmd)
    conn.close()

def add_password(master, account, password, group=None):
    path = detect_path()

    # Encrypt pass
    password = encrypt_pass(password, master)

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        if group:
            cmd = """INSERT INTO passwords(account, password, group)
                    VALUES (?, ?)"""
            c.execute(cmd, (account, password, group))
        else:
            cmd = """INSERT INTO passwords(account, password)
                    VALUES (?, ?)"""
            c.execute(cmd, (account, password))
    conn.close()

def get_password(account, master, group=None):
    path = detect_path()

    # Setup DB
    conn = sqlite3.connect(path)
    with conn:
        c = conn.cursor()
        if group:
            c.execute("SELECT * FROM passwords WHERE account=? AND group=?", (account, group))
        else:
            c.execute("SELECT * FROM passwords WHERE account=?", (account))
        password = c.fetchone()
    conn.close()

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
    conn.close()

    # Decrypt passwords
    for _ in range(len(passwords)):
        passwords[_] = decrypt_pass(passwords[_], master)

    return passwords
