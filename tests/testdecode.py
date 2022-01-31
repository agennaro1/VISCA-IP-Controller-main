# import codecs 
import codecs 
import binascii
  
s = b'I love python.'
# Using codecs.decode() method 
gfg = codecs.decode(s) 
  
print(gfg) 


print(binascii.crc32(b"hello world"))
# Or, in two pieces:
crc = binascii.crc32(b"hello")
crc = binascii.crc32(b" world", crc)
print('crc32 = {:#010x}'.format(crc))