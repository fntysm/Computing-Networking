# this is a program to encrypt the flag in the Easy Peasy picoCTF challenge
from pwn import *
KEY_LEN = 50000
MAX = 1000
# connection to the port
c = remote("mercury.picoctf.net",36981)
# going through the print prompts until this line
c.recvuntil("This is the encrypted flag!\n")
flag = c.recvlineS(keepends=False)
log.info(f"we have this Flag: {flag}")
# converting the flag from its hexadecimal given form to binary
bin_flag = unhex(flag)
counter = KEY_LEN - len(bin_flag)
with log.progress('Causing wrap-around') as dec:
    while counter > 0:
        dec.status(f"{counter} bytes left")
        chunk_size = min(MAX, counter)
        c.sendlineafter("What data would you like to encrypt? ", "a" * chunk_size)

        counter -= chunk_size

c.sendlineafter("What data would you like to encrypt? ", bin_flag)
c.recvlineS()
log.success("The flag: {}".format(unhex(c.recvlineS())))

# with help of Dvd848's writeup on github