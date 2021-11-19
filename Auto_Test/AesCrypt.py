from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64


# Crypto加解密脚本
class AesCrypt():

    def __init__(self, key, model, iv):
        self.model = {'ECB': AES.MODE_ECB, 'CBC': AES.MODE_CBC}[model]
        self.key = self.add_16(key)
        self.iv = iv.encode()
        if model == 'ECB':
            self.aes = AES.new(self.key, self.model)  # 建立aes对象
        elif model == 'CBC':
            self.aes = AES.new(self.key, self.model, self.iv)  # 建立aes对象

    def add_16(self, par):
        # python3字符串是unicode编码，须要 encode才能够转换成字节型数据
        par = par.encode('utf-8')
        while len(par) % 16 != 0:
            par += b'\x00'
        return par

    def aesdecrypt(self, text):
        # CBC解密须要从新建立一个aes对象
        if self.model == AES.MODE_CBC:
            self.aes = AES.new(self.key, self.model, self.iv)
        text = base64.decodebytes(text.encode('utf-8'))
        self.decrypt_text = self.aes.decrypt(text)
        return self.decrypt_text.decode('utf-8').strip('\0')

    def aesencrypt(self, text):
        # CBC加密须要从新建立一个aes对象
        text = str(text).encode('utf-8')
        if self.model == AES.MODE_CBC:
            self.aes = AES.new(self.key, self.model, self.iv)
        padtext = pad(text, 16, style='pkcs7')
        self.encrypt_text = self.aes.encrypt(padtext)
        self.encrypt_text = base64.b64encode(self.encrypt_text)
        return self.encrypt_text.decode('utf-8')


if __name__ == '__main__':
    # 加解密flag flag =1 是加密
    flag = 2

    key = '1raa70xiea6r1qm0'
    iv = '83h8ew1kx0gcsn4x'
    model = 'CBC'
    pr = AesCrypt(key, model, iv)

    # 注入参数加密
    word1 = """{"pageNum":1,"pageSize":10,"realName":"郑刚","phone":"123","identityCard":""}"""

    # 注入参数解密
    word2 = "rlI525yNqQkZ4jKq98qQM0QpgN67tNN5ZR+sDsUY4rfVeKGgd2WqTVe+piFKABGydM1EdT5X4uaY/ueWNbLxwQ+hpq1U4Bzp85OIGEFY/ao="
    # 解密
    # print(pr.aesdecrypt(word))
    # 加密
    if flag == 1:
        # 加密
        print(pr.aesencrypt(word1))
    else:
        # 解密
        print(pr.aesdecrypt(word2))
