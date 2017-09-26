#!/usr/bin/env python2

from Crypto.PublicKey import RSA

RSAkey = RSA.generate(2048)
p = getattr(RSAkey.key, 'p')
q1 = getattr(RSAkey.key, 'q')
RSAkey = RSA.generate(2048)
q2 = getattr(RSAkey.key, 'q')
f = open('primes.txt','w')
f.write('p = ' + str(p))
f.write('\n\nq1 = ' + str(q1))
f.write('\n\nq2 = ' + str(q2))
f.write('\n\nrsa1 = ' + str(p*q1))
f.write('\n\nrsa2 = ' + str(p*q2) + '\n')
f.close()
