ingredients = ["water", "milk", "black tea"]
# In tuple we can try to change the value add in where it is defined  
# Tuple -> Once its defined, I cannot it throught the lifecycle of a program.

ingredients.append("sugar")
print(f"ingredients are: {ingredients}")
ingredients.remove("water")
print(f"ingredients are: {ingredients}")


# lots of methods available in the world of the list

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

# extend - always add the elements at the end
chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")

# insert - always add the element at the given index
# append - always add the element at the end
chai_ingredients.insert(2,"black tea")
print(f"Chai: {chai_ingredients}")

# Remove somthing form particular position
# pop - always remove the last element
last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"Chai: {chai_ingredients}")

# Reverse - each postion will be reversed
chai_ingredients.reverse()
print(f"Reverse Chai: {chai_ingredients}")

# Sort - each postion will be sorted
chai_ingredients.sort()
print(f"Sorted Chai: {chai_ingredients}")	

sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level:{max(sugar_levels)}")
print(f"Minimum sugar level:{min(sugar_levels)}")