# Find the first Non- Repeated Character 

# Given a string, find the first non-repeated character 


input_str = "teeteracdacd"



for char in input_str:
    # print(char)
    if input_str.count(char) == 1:
        print("Char is: ",char)
        break                        # as to find only first non-repeated character so break the loop as found --> optimized
