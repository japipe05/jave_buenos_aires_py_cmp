import os
import hashlib

def hash_password(password):
    # Genera una sal aleatoria
    salt = os.urandom(32)
    # Hash de la contraseña con sal usando SHA-256
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + hashed_password

def verify_password(stored_password, provided_password):
    for r in stored_password:
        r
    # Decodifica la cadena hexadecimal almacenada en bytes
    stored_password_bytes = bytes.fromhex(r.credencial)
    # Extrae la sal (primeros 32 bytes)
    salt = stored_password_bytes[:32]
    # Extrae el hash almacenado (resto de los bytes)
    stored_hash = stored_password_bytes[32:]
    # Genera un nuevo hash con la sal recuperada y la contraseña proporcionada
    new_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    # Compara el hash generado con el hash almacenado
    return new_hash == stored_hash