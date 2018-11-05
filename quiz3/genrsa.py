from fractions import gcd
from Crypto.Util import number

BITS = 4

p = number.getPrime(BITS)
q = number.getPrime(BITS)
n = p*q

print(p,q,n)
