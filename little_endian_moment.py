import struct

x = 213

# Pack integer into bytes using native byte order
b = struct.pack('I', x)

if b[0] == 1:
    print("Little Endian")
else:
    print("Big Endian")