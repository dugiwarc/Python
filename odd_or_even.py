number = int(input("Enter a number: "))
divisor = int(input("Enter a divisor: "))

remainder = number % divisor

if number % divisor == 0:
	print(str(divisor) + " divides " + str(number))
else:
	print(str(divisor) + " divides " + str(number) + ' with a ' + str(remainder) + ' remainder')
# elif number % 4 == 0:
# 	print("You have entered a multiple of 4.")
# elif number % 2 != 0:
# 	print("You have entered an odd number.")
# else:
# 	print("You have entered an even number.")