'''
Created on Nov 23, 2017

@author: sreenivasaraomolakalapalli
'''
from Crypto.Cipher import AES
import os
from itsdangerous import base64_encode, base64_decode

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

# key = os.urandom(16) # the length can be (16, 24, 32)
key = b'1234567890123456'
text = 'KEhxK/2KmmlGtevNtm9eFTTGivCawaIwyFPPRMbcyqA='
IV = b'1234567890123456'
#cipher = AES.new(key, AES.MODE_CBC, IV=IV)

#data = base64_encode(cipher.encrypt(pad(text)))

#print data
#
cipher = AES.new(key, AES.MODE_CBC, IV=IV)
print cipher.decrypt(base64_decode(text))