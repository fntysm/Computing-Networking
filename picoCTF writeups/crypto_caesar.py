import string
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(plain):
    dec = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        dec += ALPHABET[int(binary[:4], 2)]
        dec += ALPHABET[int(binary[4:], 2)]
    return dec


def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

