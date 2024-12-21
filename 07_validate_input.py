# Validate Input

# Keep asking the user for input until they enter a number between 1 to 10


# agar no. 1-10 ke bich mein nahi hai to infinite loop chalake input lo aur agar hai toh ruk(break) jao

while True:

    input_number = int(input("Enter a number b/w 1-10: "))
    if 1<= input_number <= 10:           # assigned condition
        print("Thanks")
        break
    else:
        print("Invalid Number, Try Again!")     #  not assigned any condition since want to run the loop again and again
