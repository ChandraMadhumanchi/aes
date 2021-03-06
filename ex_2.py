import base64

from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        #raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        #cipher = AES.new( self.key, AES.MODE_CBC, iv )
        cipher = AES.new( self.key, AES.MODE_CTR)
        #return base64.b64encode( iv + cipher.encrypt( raw ) )
        return base64.b64encode(cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CTR )
        return cipher.decrypt( enc[16:] )


cipher = AESCipher('mysecretpassword')
encrypted = cipher.encrypt('HelloWorld')
decrypted = cipher.decrypt(encrypted)
print encrypted
print decrypted