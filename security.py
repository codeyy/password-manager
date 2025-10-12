import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet

DEFAULT_ITERATIONS = 200_000
SALT_SIZE = 16

def gen_salt():
    """Generate a random salt."""
    return os.urandom(SALT_SIZE)

def derive_key(master_password: str, salt: bytes, iterations: int = DEFAULT_ITERATIONS) -> bytes:
    password_bytes = master_password.encode('utf-8')
    """Derive a secure key from the given password and salt."""
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = DEFAULT_ITERATIONS,
    )
    return urlsafe_b64encode(kdf.derive(password_bytes))

def encrypt_data(key: bytes, plaintext: str) -> bytes:
    cypher = Fernet(key)
    return cypher.encrypt(plaintext.encode())

def decrypt_data(key: bytes, ciphertext: bytes) -> str:
    cypher = Fernet(key)
    return cypher.decrypt(ciphertext).decode()