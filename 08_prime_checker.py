# Check if a number is prime



number = int(input("Enter the Numeber: "))

is_prime = True     # assuming every no. is prime no.

if number > 1:
    for i in range(2,number):   # checking from 2 to number 
        if number % i == 0:
            is_prime = False
            break

print("Prime: ",is_prime)