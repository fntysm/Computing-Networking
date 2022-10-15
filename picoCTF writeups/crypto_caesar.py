import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_decode(plain):
    dec = ""
    for c in range(0, len(plain), 2):
        unbinary = ""
        unbinary += "{0:b}".format(ALPHABET.index(plain[c])).zfill(4)
        unbinary += "{0:b}".format(ALPHABET.index(plain[c + 1])).zfill(4)
        dec += chr(int(unbinary, 2))
    return dec


def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

flag = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
for key in ALPHABET:
    dec = ""
    for i, c in enumerate(flag):
      dec += unshift(c, key[i % len(key)])

    dec = b16_decode(dec)
    print(dec)