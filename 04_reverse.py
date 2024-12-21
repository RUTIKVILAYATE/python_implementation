# Reverse a string using  a loop

input_string = input("Enter a string: ")
reversed_str = " "

for char in input_string:     # string ke har ek char ke liye usko ek empty string mein concatenate krdo 
    reversed_str = char +  reversed_str     # reverse concatenate krdo --> "P" + "" --> P, y+P --> yP
print(reversed_str)
