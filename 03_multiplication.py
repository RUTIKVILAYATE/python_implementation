# Multiplication table printer

# Problem: Print the multiplication table for the given number up to 10, but skip the fifth iteration 


number = 3
# num = int(input("Enter the Number: "))

for i in range(1,11):      
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)
    
    



# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 2 = 9

