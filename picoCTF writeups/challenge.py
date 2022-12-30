import string

#'JyvCCDrKvJ{s8LKVWhItk_3rf_tFDk_yl4uP}'
#'shellmates{}'
flag = 'shellmates'
key = 17

possible_chars = string.ascii_letters + string.digits
n = len(possible_chars) # 62
enc = ''

for c in flag :
    if c in possible_chars :
        i = possible_chars.index(c)
        enc += possible_chars[(i + key) % n]
        print("i : ", i, " et c :  ", c," et enc : ",enc)
    else :
        enc += c

print(enc)