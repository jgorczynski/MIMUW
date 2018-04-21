s = b'UHl0aG9uIGplc3QgZmFqbnkg8J+Yjg==\n'

import codecs
b64 = codecs.decode(s, 'base64')

inUTF8 = b64.decode('utf8')
print(str(inUTF8))
