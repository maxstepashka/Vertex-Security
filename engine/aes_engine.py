# AES engine
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import hashlib

def generate_key(length):
    return os.urandom(int(length/8)).hex()

def encrypt_text(text_str, key_hex):
    text = text_str.encode('UTF-8')
    key = bytes.fromhex(key_hex)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    padded_data = padder.update(text) + padder.finalize()
    ciphertext = iv + encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt_text(ciphertext, key_hex):
    key = bytes.fromhex(key_hex)
    iv=ciphertext[:16]
    ciphertext = ciphertext[16:] 
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()

    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data.decode('UTF-8')

def decrypt_text_for_rsa(ciphertext, key_hex):
    key = bytes.fromhex(key_hex)
    iv=ciphertext[:16]
    ciphertext = ciphertext[16:] 
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()

    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data

def encrypt_file(text_file, key_hex):
    text=read_file(text_file)
    key = bytes.fromhex(key_hex)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    padded_data = padder.update(text) + padder.finalize()
    ciphertext = iv + encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt_file(ciphertext_file, key_hex):
    ciphertext=read_file(ciphertext_file)
    key = bytes.fromhex(key_hex)
    iv=ciphertext[:16]
    ciphertext = ciphertext[16:] 
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()

    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data

def write_file(path, byte_str):
    with open(path, 'wb') as output_file:
        output_file.write(byte_str)

def read_file(path):
    with open(path, 'rb') as input_file:
        byte_str=input_file.read()
        return byte_str
# Разработчик! Не забывай убирать нижние строки перед запуском!
# s='{"Моя связка ключей": {"type": "RSA_PAIR", "value": {"priv": "C:\\\\Users\\Max\\Desktop\\\\keys\\private.pem", "pub": "C:\\\\Users\\\\Max\\\\Desktop\\\\keys\\\\public.pem"}}, "Публичный ключ Антонова": {"type": "RSA_PUB", "value": {"pub": "C:\\\\Users\\\\Max\\\\Desktop\\\\keys\\\\public.pem"}}, "Мой ключ от AES": {"type": "AES", "value": {"key": "37f8bcf372e2e0ea0a6dddf294a051e28b3ed7f3e3698212"}}, "Мой ключ от Blowfish": {"type": "Blowfish", "value": {"key": "39f83cff72e2d0eaaa6dddf294a051e28b3ed7f3e3698212"}}, "Наш секретный ключ": {"type": "AES", "value": {"key": "37f8bcf372e2e0ea0a6dddf294a051e28b3ed7f3e3698212"}}}'
# print(s[64])
# write_file('C:\\Users\\Max\\Yandex.Disk\\Documents\\programming\\Python\\Vertex\\files\\keys.json', encrypt_text(s, hashlib.sha256('z'.encode('UTF-8')).hexdigest()))