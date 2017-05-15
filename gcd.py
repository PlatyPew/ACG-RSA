#!/usr/bin/env python2

x = long(raw_input('RSA public key 1 > '))
y = long(raw_input('RSA public key 2 > '))

# Make x smaller than y
if x > y:
	tmp = y
	y = x
	x = tmp

rsa1 = x
rsa2 = y

# Calculate GCD
while True:
	r = y % x
	y = x
	if r == 0:
		break
	x = r

print '\n---------- Primes ----------'
print 'p = ' + str(rsa1/x)
print 'q = ' + str(x)
print ''
print 'p = ' + str(rsa2/x)
print  'q = ' + str(x)
