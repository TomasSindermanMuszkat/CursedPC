
import glob
from cryptography.fernet import Fernet

with open("key", "rb") as key:
    crypt = Fernet(key.read())

def encrypt_file(filepath):
    with open(filepath, "rb") as fread:
        data = fread.read()
    with open(filepath, "wb") as fwrite:
        fwrite.write(crypt.encrypt(data))
    os.rename(filepath, filepath+".enc")

def encrypt_dir(root):
    files = glob.glob(root + "/*", recursive=True)
    # Filter out files that are already encrypted, else it will make
    # -decrypting difficult.
    files_not_encrypted = list(filter(lambda f: not f.endswith(".enc"), files))
    for filepath in list(files_not_encrypted):
        print("Encrypting {}...".format(filepath))
        encrypt_file(filepath)

encrypt_dir("testdir")
