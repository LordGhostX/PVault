# Database Handler
from getpass import getpass
from platform import system
from crypt import hash_pass
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

def create_database():
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
