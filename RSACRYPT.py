# an algorithm to decrypt a RSA encryption
# cipher text
c= 861270243527190895777142537838333832920579264010533029282104230006461420086153423
# multiply of 2 prime numbers (p and q)
p = 670577792467509699665091201633524389157003
q = 1955175890537890492055221842734816092141
n= 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
# 1 < e < fi(N)
e= 65537
# with fi(N)=(p-1)(q-1)
fi = (p-1)*(q-1)
# calculating the private key: d^e mod fi == 1
d = pow(e, -1, fi)
# solve for the answer
answer = pow(c, d, n)
# print the answer
print(bytes.fromhex(hex(answer)[2:]).decode('ascii'))

