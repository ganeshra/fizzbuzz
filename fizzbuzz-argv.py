import sys

if len(sys.argv) == 1:
	t = int(raw_input("Enter some number for Fizzbuzz-"))
else:
	t = int(sys.argv[1])
print "FizzBuzz counting up to",t
i = 1
while i <= t:
	if i % 3 == 0 and i % 5 == 0:
		print "fizzbuzz"
	elif i % 3 ==0:
		print "fizz"
	elif i % 5 == 0:
		print "buzz"
	else:
		print i
	i = i+1
