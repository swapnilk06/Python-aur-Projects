essential_spices = {"cardamom", "ginger", "cinnamon"}

optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}") # Get all of them, but don't get the reputation

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}") # Only that which is common between both of them.

only_in_essential = essential_spices - optional_spices # ignoreing the common form essential
print(f"Only in essential spices: {only_in_essential}")
only_in_optional = optional_spices - essential_spices # # ignoreing the common form optional
print(f"Only in optinal spices: {only_in_optional}")

# Membership test
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

