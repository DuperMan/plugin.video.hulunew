def AES(key):
    #try:
    from Crypto.Cipher import AES
    return AES.new(key, AES.MODE_ECB)
    #except ImportError:
    #    from crypto.cipher.rijndael import Rijndael
    #    from crypto.cipher.base     import noPadding
    #    return Rijndael(key, keySize=32, blockSize=16, padding=noPadding())
    
def AES_CBC(key):
    #try:
    from Crypto.Cipher import AES
    return AES.new(key, AES.MODE_CBC)
    #except ImportError:
    #    from crypto.cipher.rijndael import Rijndael
    #    from crypto.cipher.base     import noPadding
    #    return Rijndael(key, keySize=32, blockSize=16, padding=noPadding())