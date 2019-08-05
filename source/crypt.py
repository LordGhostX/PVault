# Anything Cryptography
from hashlib import md5, sha256, sha512
from pyAesCrypt import encryptFile, decryptFile
from os import remove
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64

def gen_key(master, salt):
    # Generate Fernet key
    password = master.encode()
    salt = salt.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key

def hash_rounding(word, algo="sha512", rounds=100, salt="@8fh::=G=-,./~~}%]"):
    # Continual reversal hashing for a given word to make it more harder to crack
    if algo == "md5":
        algo = md5
    elif algo == "sha256":
        algo = sha256
    else:
        algo = sha512
    hash = word
    for round in range(rounds):
        # hash the password with it's salt and reverse it to make it harder to crack
        hash = algo((hash + salt).encode()).hexdigest()[::-1]

    return hash

def hash_pass(word, algo="sha512", salt="Gu6#&3_==[';;/~~"):
    # Hashes a given password
    hash = word
    hash = hash_rounding(hash, algo="md5", salt=salt) + hash_rounding(hash, algo="sha256", salt=salt) + hash_rounding(hash, algo="sha512", salt=salt)
    hash = hash_rounding(hash, algo=algo)

    return hash

def encrypt_pass(plain_pass, master_password):
    # Encrypt a password with Fernet
    key = gen_key(master_password, hash_pass(master_password))
    encryptor = Fernet(key)
    del key
    hashed_pass = encryptor.encrypt(plain_pass.encode())

    return hashed_pass.decode()

def decrypt_pass(hashed_pass, master_password):
    # Decrypts an encrypted password with Fernet
    key = gen_key(master_password, hash_pass(master_password))
    decryptor = Fernet(key)
    del key
    dehashed_pass = decryptor.decrypt(hashed_pass.encode())

    return dehashed_pass.decode()

def encryptDB(file, master, inplace=True):
    # Encrypt the database with AES256-CBC
    try:
        encryptFile(file, file+".aes", master, 64 * 1024)
        if inplace:
            remove(file)
        return True
    except:
        return False

def decryptDB(file, master, inplace=True):
    # decrypt the AES256-CBC encrypted database
    try:
        decryptFile(file+".aes", file, master, 64 * 1024)
        if inplace:
            remove(file+".aes")
        return True
    except:
        return False
