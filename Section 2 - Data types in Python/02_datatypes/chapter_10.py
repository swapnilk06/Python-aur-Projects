chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")
# Always remember in the dictionary "order dosn't really matter"

# How we add the data, accessing data.. in dept
chai_recipe = {} # Common way of creating an Empty dictionary

# add more data with [""]
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# access data
print(f"Recipe: {chai_recipe}") # whole thing in output
print(f"Recipe base: {chai_recipe['base']}")

# "del" => to delete any component inside a dictionary
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print("-------------------")

# membersip test
print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}
print(f"Chai order: {chai_order}")

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")

print("-------------------")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

print("-------------------")

# get size
chai_size = chai_order["size"]
print(f"Chai size is: {chai_size}")

# Want to get not exist key
# chai_size = chai_order["customer_note"]
# print(f"Chai size is: {chai_size}")
# That crash whole system

# good code with get - That way not crashing whole system
# dosn't crash whenever value can't find it, I can provide the default value
customer_note = chai_order.get("Medium", "No Note")
print(f"Customer note is: {customer_note}")

customer_note = chai_order.get("size", "No Note")
print(f"Customer note is: {customer_note}")