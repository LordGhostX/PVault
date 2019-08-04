# Anything Cryptography
from hashlib import md5, sha256, sha512

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
        hash = algo((hash + salt).encode()).hexdigest()[::-1]

    return hash

def hash_pass(word, algo="sha512", salt="Gu6#&3_==[';;/~~"):
    # Hashes a given password
    hash = hash_rounding(hash, algo="md5", salt=salt) + hash_rounding(hash, algo="sha256", salt=salt) + hash_rounding(hash, algo="sha512", salt=salt)

    hash = hash_rounding(hash, algo=algo)

    return hash

def encrypt_pass(plain_pass, master_password):
    return plain_pass

def decrypt_pass(hashed_pass, master_password):
    return hashed_pass
