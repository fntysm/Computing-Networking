# this one is to test random and simple specific lines
import string
flag = 'JyvCCDrKvJ{s8LKVWhItk_3rf_tFDk_yl4uP}'
key = 17

possible_chars = string.ascii_letters + string.digits
n = len(possible_chars) # 62
dec = ''

for c in flag :
    if c in possible_chars :
        i =  possible_chars.index(c)
        dec += possible_chars[(i - key) % n]
    else :
        dec += c

print(dec)