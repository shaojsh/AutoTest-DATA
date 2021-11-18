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
    key = '1raa70xiea6r1qm0'
    iv = '83h8ew1kx0gcsn4x'
    model = 'CBC'
    pr = AesCrypt(key, model, iv)

    # 注入参数加解密
    word = 'PiPzX8/fVg08OOoCD61zr42+/GRAC5l8GzrkXZFoL72vWaXlWogxy6shQLfQK/Px'
    # 解密
    # print(pr.aesdecrypt(word))
    # 加密
    print(pr.aesencrypt(word))