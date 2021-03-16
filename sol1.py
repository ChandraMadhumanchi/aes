'''
Created on Nov 23, 2017

@author: sreenivasaraomolakalapalli
'''
from Crypto.Cipher import AES
from itsdangerous import base64_encode,base64_decode

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

# key = os.urandom(16) # the length can be (16, 24, 32)
#key = b'1234567890123456'
key = b'DMWlS5qiSrCyS6urKR/gXQ=='
text = 'CTJO21Vl+YUO5T9wu/JV6g=='
text1 = pad(text)
cipher = AES.new(base64_decode(key))
#print base64_encode(cipher.encrypt(pad(text)))
#print cipher.decrypt(base64_decode(base64_encode(cipher.encrypt(pad(text)))))
print cipher.decrypt(base64_decode(text))