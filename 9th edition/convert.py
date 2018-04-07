#hex
h1, h2, h3 = 0x1F, int('0x1F', 0), int('1F', 16)
#oct
o1, o2, o3 = 0o17, int('0o17', 0), int('17', 8)
#bin
b1, b2, b3 = 0b101, int('0b101', 0), int("101", 2)

#print("", h1,o1,b1, "\n",h2,o2,b2, "\n",h3,o3,b3)

a, b = 3, 13
c = (a+b)*b
s = "(" + bin(a) + " + " + oct(b) + ") * " + hex(b) + " = " + str(c)
#print(s)

#unicode, chr(), ord(), \uNNNN

"""print(chr(0x21c4) + " == \u21c4 == ⇄")
print(hex(ord("⇄")), hex(ord("\u21c4")), hex(ord(chr(0x21c4))) )"""

#encoding

a = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
inUTF7 = a.encode('utf7')
inUTF8 = a.encode()
print(a + "\nw utf7 to: " + str(inUTF7) + "\nw utf8: " + str(inUTF8))

print("zdekodowany UTF7: " + inUTF7.decode('utf7'))

import codecs
b64 = codecs.encode(inUTF8, 'base64')
print('napis w UTF8 po zakodowaniu base64 to: ' + str(b64))
