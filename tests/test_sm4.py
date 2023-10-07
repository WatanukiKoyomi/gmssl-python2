# coding=utf-8
import gmssl.func
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

key = '3l5butlj26hvv313'  # 密钥的类型是16位字符串
value = '111'
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
crypt_sm4 = CryptSM4()

crypt_sm4.set_key(key, SM4_ENCRYPT)
encrypt_value = crypt_sm4.crypt_ecb(value)
print 'encrypt_value'
print encrypt_value
print gmssl.func.bytes_to_list(encrypt_value)
crypt_sm4.set_key(key, SM4_DECRYPT)
decrypt_value = crypt_sm4.crypt_ecb(encrypt_value)
print 'decrypt_value'
print decrypt_value

# crypt_sm4.set_key(key, SM4_ENCRYPT)
# encrypt_value = crypt_sm4.crypt_cbc(iv , value)
# crypt_sm4.set_key(key, SM4_DECRYPT)
# decrypt_value = crypt_sm4.crypt_cbc(iv , encrypt_value)
# print decrypt_value
