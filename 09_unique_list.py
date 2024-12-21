# List Uniqueness Checker
# check if all elements in the list are unique, if the duplicate is found exit the loop and print duplicate

# create a empty list which takes all the values(string) from the user

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:     # item ke ek item
    if item in unique_item:   # agar set mein hai
        print("Duplicate: ", item)   # toh usko duplicate bolo
        break                        # duplicate hai toh ruk jao
    unique_item.add(item)            # aur nahi hai toh set mein woh item daalo
    




# agar list hai aur ek set hai
# toh set mein agr list ka item nahi hai 
# toh set mein woh item daalo 
# aur agr set mein woh item hai 
# toh woh item mat daalo 
# aur woh item direct print krdo
# matlab ki duplicate item khoj daalo

# 