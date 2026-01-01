# RSA engine
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from engine import aes_engine

def generate_keys(length):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=length,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def write_keys(private_key, public_key, folder_name, password):
    private_pem=private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(password=password.encode('UTF-8')))
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)
    with open(f'{folder_name}\\private.pem', 'wb') as private_f:
        private_f.write(private_pem)
    with open(f'{folder_name}\\public.pem', 'wb') as public_f:
        public_f.write(public_pem)

def load_private_key(private_f_name, password):
    with open(private_f_name, "rb") as private_key_f:
        private_key = serialization.load_pem_private_key(private_key_f.read(), password=password.encode('UTF-8'))

    return private_key

def load_public_key(public_f_name):
    with open(public_f_name, "rb") as public_key_f:
        public_key = serialization.load_pem_public_key(public_key_f.read())
    
    return public_key

def encrypt_text(text_str, public_key): 
    key=aes_engine.generate_key(128)
    ciphertext=aes_engine.encrypt_text(text_str, key)
    key_ciphertext = public_key.encrypt(
        key.encode('UTF-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return key_ciphertext, ciphertext

def decrypt_text(ciphertext, private_key):

    text = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return text.decode('UTF-8')

def encrypt_file(text_file, public_key): 
    key=aes_engine.generate_key(128)
    ciphertext=aes_engine.encrypt_file(text_file, key)
    key_ciphertext = public_key.encrypt(
        bytes.fromhex(key),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return key_ciphertext + '\n-----CIPHERTEXT-----\n'.encode('UTF-8') + ciphertext

def decrypt_file(ciphertext_file, private_key):
    serialized_ciphertext=read_file(ciphertext_file).split(b'\n-----CIPHERTEXT-----\n')
    key_ciphertext=serialized_ciphertext[0]
    ciphertext=serialized_ciphertext[1]
    key = private_key.decrypt(
        key_ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).hex()
    text=aes_engine.decrypt_text_for_rsa(ciphertext, key)
    return text

def write_file(path, byte_str):
    with open(path, 'wb') as output_file:
        output_file.write(byte_str)

def read_file(path):
    with open(path, 'rb') as input_file:
        byte_str=input_file.read()
        return byte_str