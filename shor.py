
# Calculate GCD
def gcd(x,N):
	while True:
		r = N % x
		N = x
		if r == 0:
			break
		x = r
	return x

# Calculate period
def period(x,N):
	i = 1
	while True:
		ans = (x ** i) % N
		if i % 10000 == 0:
			print i
		if ans == 1:
			break
		i += 1
	return i

# Main function
def main():
	N = int(raw_input('Input number to factorise > '))
	x = int(raw_input('Input random number smaller than N > '))

	if gcd(x,N) != 1:
		print str(x) + ' is invalid as it is not relatively prime'
		exit()

	r = period(x,N)
	if r % 2 != 0:
		print str(x) + ' is invalid as the period is not divisible by 2'
		exit()

	factor1 = (x**(r/2)+1)
	factor2 = (x**(r/2)-1)
	print 'First factor = ' + str(gcd(factor1,N))
	print 'Second factor = ' + str(gcd(factor2,N))

# Initiate main function
if __name__ == '__main__':
	main()
