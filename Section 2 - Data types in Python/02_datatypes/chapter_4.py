# Boolean
is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling #upcasting -> True automatically convert into 1

print(f"Total actions: {total_actions}")

# milk_present = 0 # no milk -> # False
# milk_present = 1 # milk -> # True
# milk_present = 11 # True
milk_present = "swapnil" # True
milk_present = None # False

print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")