import base64
import binascii

from gmssl.func import bytes_to_list

from gmssl import sm2, func


def test_sm2():
    # private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
    # private_key = '0B1CE43098BC21B8E82B5C065EDB534CB86532B1900A49D49F3C53762D2997FA'
    private_key = 'd9d37f4f46e8514c6f9398a984e74f3eead994e8f4ac5f92e5deb313cb5ad6a6'
    # public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
    public_key = 'e332ee43ac37be458550652fb9de9d58faf4bea2567534fda3319212a55b0732f5a9b7304b3a0127355ef98419b3a3598d0108611d658839e5d603abe01683ea'
    sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=private_key)
    data = "123456"
    enc_data = sm2_crypt.encrypt(data)
    java_data = 'R6p5ewq/eOXsAK+3tIglU6SHyLaMuAd8df61u2sX+oMzwE4nsEFElIY29ERna11JaTZeA2U2h4+4LqdhBipAyuRO4JOrxvT5c6twgfH64nsyfykS1AkLSIqminwsyj1knEL3QEc9vRwuBA=='
    enc_data = base64.standard_b64decode(java_data)
    dec_data = sm2_crypt.decrypt(enc_data)
    bytes_list = bytes_to_list(dec_data)
    print(b"dec_data:%s" % dec_data)
    print(b"dec_data:%s" % bytes_list)
    # assert data == dec_data

    print("-----------------test sign and verify---------------")
    random_hex_str = func.random_hex(sm2_crypt.para_len)
    sign = sm2_crypt.sign(data, random_hex_str)
    print('sign:%s' % sign)
    verify = sm2_crypt.verify(sign, data)
    print('verify:%s' % verify)
    assert verify


def test_sm2sm3():
    private_key = "3945208F7B2144B13F36E38AC6D39F95889393692860B51A42FB81EF4DF7C5B8"
    public_key = "09F9DF311E5421A150DD7D161E4BC5C672179FAD1833FC076BB08FF356F35020CCEA490CE26775A52DC6EA718CC1AA600AED05FBF35E084A6632F6072DA9AD13"
    random_hex_str = "59276E27D506861A16680F3AD9C02DCCEF3CC1FA3CDBE4CE6D54B80DEAC1BC21"
    print private_key.__len__()
    print public_key.__len__()
    sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=private_key)
    data = b"message digest"

    print("-----------------test SM2withSM3 sign and verify---------------")
    enc_data = sm2_crypt.encrypt(data)
    print base64.standard_b64encode(enc_data)
    # print("enc_data:%s" % enc_data)
    # print("enc_data_base64:%s" % base64.b64encode(bytes.fromhex(enc_data)))
    dec_data = sm2_crypt.decrypt(enc_data)
    print(b"dec_data:%s" % dec_data)
    assert data == dec_data
    sign = sm2_crypt.sign_with_sm3(data, random_hex_str)
    print('sign: %s' % sign)
    verify = sm2_crypt.verify_with_sm3(sign, data)
    print('verify: %s' % verify)
    assert verify


if __name__ == '__main__':
    test_sm2()
    # test_sm2sm3()
