chai_type = "Ginger chai"
customer_name = "Priya"


print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold" # Indexing => A=0, r=1 
# Last number in not inclusive

print(f"First word: {chai_description[0:8:1]}") # '1' means every single character

print(f"Second word: {chai_description[0:8:2]}") # '2' => means every second character

print(f"Last word: {chai_description[0:8]}") 