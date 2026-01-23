#! python3

from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher

class CryptographyProcesses:
    def __init__(self):
        pass

    def string_encryption(self, data: str) -> tuple:
        import secrets
        key = secrets.token_bytes(32)
        nonce = secrets.token_bytes(16)
        cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
        encryptor = cipher.encryptor()
        return (encryptor.update(data) , key, nonce)
        
    def file_encryption(self, fp: str, ekey: bytes, enonce: bytes):
        import os
        cipher = Cipher(algorithms.AES(ekey), modes.CTR(enonce))
        encryptor = cipher.encryptor()
        with open(fp, 'rb') as inf, open(fp+'.encryted', 'wb') as destf:
            while True:
                chunk = inf.read(5024*5024)
                if not chunk:
                    break
                destf.write(encryptor.update(chunk))
        os.unlink(fp)
                
            
