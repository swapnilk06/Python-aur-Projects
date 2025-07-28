from base64 import encode

chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold" 
# Indexing means each letter in this string is represented by a number => A=0, r=1, o=2,...,c=7

# Last number is not inclusive in the world of python 

# Without include 'c' in => 0 to 7 indexing
print(f"First word: {chai_description[0:7]}")

print(f"Second word: {chai_description[0:8:1]}") # '1' => means every single character
# print(f"Second word: {chai_description[0:8:2]}") # '2' => means every second character

# Pythonic way doing above
print(f"Third word: {chai_description[:11]}") 
print(f"Forth word: {chai_description[12:]}") 
# print(f"Third word: {chai_description[::8]}") 
# print(f"Forth word: {chai_description[12::]}") 

print(f"Last word: {chai_description[::-1]}") # '-1' shorthand for reversing the whole string

# label_text = "Chai Special"
label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")
