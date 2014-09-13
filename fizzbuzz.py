t = int(raw_input("Enter number to run FizzBuzz-"))
print "FizzBuzz counting up to ",t
for i in range(1,t+1):
	if i % 3 == 0 and i % 5 == 0:
		print "fizzbuzz"
	elif i % 3 ==0:
		print "fizz"
	elif i % 5 == 0:
		print "buzz"
	else:
		print i
