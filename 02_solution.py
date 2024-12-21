# Sum of even numbers

# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter the Number to which U want Sum Even Numbers: "))

sum_even = 0

for i in range(1,n+1):
    if i%2==0:
        sum_even = sum_even + 1
print("Sum of Even Numbers: ",sum_even)