'''
Encryption and decryption functions for files
'''
from os import rename
from glob import glob
from cryptography.fernet import Fernet

def write_key():
    '''
    Generates a key and save it into a file
    '''
    # Create encryption key
    key = Fernet.generate_key()
    # Save it into "key" file
    with open("key", "wb") as key_file:
        key_file.write(key)

def read_key():
    '''
    Reads the key from the key file
    '''
    with open("key", "rb") as key_file:
        return key_file.readline()

def encrypt_file(filepath, key):
    '''
    Encrypts the given file with the given key
    '''
    # Instance key
    crypt = Fernet(key)
    # Read decrypted file
    with open(filepath, "rb") as fread:
        data = fread.read()
    # Write it into an encrypted file
    with open(filepath, "wb") as fwrite:
        fwrite.write(crypt.encrypt(data))
    # Add the ".enc" extension
    rename(filepath, filepath+".enc")

def decrypt_file(filepath, key):
    '''
    Decrypts the given file with the given key
    '''
    # Instance key
    crypt = Fernet(key)
    # read encrypted file
    with open(filepath, "rb") as fread:
        data = fread.read()
    # Write it into a decrypted file
    with open(filepath, "wb") as fwrite:
        fwrite.write(crypt.decrypt(data))
    # Remove the ".enc" extension
    rename(filepath, filepath.rstrip(".enc"))

def encrypt_dir(root):
    '''
    Calls the encryption function for each file in the given directory
    '''
    # Lists the files in the directory
    files = glob(root + "/*", recursive=True)
    # Filter out files that are already encrypted, else it will make
    # -decrypting difficult.
    files_not_encrypted = filter(lambda fp: not fp.endswith(".enc"), files)
    # Call the encryption function for each unencrypted file in the folder
    for filepath in list(files_not_encrypted):
        print("Encrypting \"{}\"...".format(filepath))
        encrypt_file(filepath, read_key())

def decrypt_dir(root):
    '''
    Calls the Decryption function for each file in the given directory
    '''
    # Lists the files in the directory
    files = glob(root + "/*", recursive=True)
    # Filter out files that are not encrypted, else it will make
    # -decrypting difficult.
    files_encrypted = filter(lambda fp: fp.endswith(".enc"), files)
    # Call the decryption function for each unencrypted file in the folder
    for filepath in list(files_encrypted):
        print("Decrypting \"{}\"...".format(filepath))
        decrypt_file(filepath, read_key())

encrypt_dir("testdir")
decrypt_dir("testdir")
