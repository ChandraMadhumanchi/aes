'''
Created on Nov 23, 2017

@author: sreenivasaraomolakalapalli
'''

import base64
import binascii
import hashlib

from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16  # Bytes

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


# unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:
    __slots__ = ['key', 'text']

    def __init__(self, key):
        self.key = key
        # key_value = hashlib.sha512(key).digest()
        print("key vaule {} {}".format(self.key,len(self.key)))

    def encrypt(self, text):
        #pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
        text = pad(text)
        print("text {} {}".format(text , len(text)))
        iv = b"0000000000000000" #iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_ECB)#, iv)
        try:
            return base64.b64encode(cipher.encrypt(text))
        except:
            text = ' '
            print("error")
            #return base64.b64decode(cipher.encrypt(text))
            # return base64.b64encode(cipher.encrypt(text))

    def decrypt(self, text):
        text = base64.b64decode(text)
        # iv = text[:16]
        iv = b"0000000000000000" #iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_ECB)#, iv)
        # = AES.new(self.key, AES.MODE_CBC)
        # return unpad(cipher.decrypt( text[16:] ))
        return unpad(cipher.decrypt(text))


if __name__ == "__main__":
    key = binascii.a2b_base64("fYzdKt06PKI3zVGAfzYwgdDUApzG6VVqf25FQTJoZac=")
    #key = "fYzdKt06PKI3zVGAfzYwgdDUApzG6VVqf25FQTJoZac=".encode()
    cipher_object = AESCipher(key)
    str_input = "Sleep and Work and Sleep"
    print ("str_input {}".format(str_input))
    encrypted = cipher_object.encrypt(str_input)
    encrypted_str = binascii.b2a_base64(encrypted).decode()
    print(encrypted_str)

    #encrypted_str = "cpPUwexL7Ga2fgLsR38zGNyzC2Pka6YzYrlpngUGwCQ="

    decrypted_str = cipher_object.decrypt(binascii.a2b_base64(encrypted_str.encode())).decode()

    print ("decrypted_str {} ".format(decrypted_str))