# Python - Learn by Building Projects : Section 3

## Section 3: Conditionals in Python

### 21] Kettle Boiling Story Project

#### Conditionals Challenge

- You're creating a notification system for a smart kettle.
- It should remind the user only when the kettle has finished boiling.

  - A variable `kettle_boiled = True`
  - If boiled, show: `"Kettle done! Time to make chai!"`

- [x] We have to convert the problem into solution & that solution needs to be delivered via software.

---

> [!IMPORTANT]

### Coding Exercise

- [x] Customer Discount Eligibility
      You’re building a logic module for a billing system. Based on customer data, you need to evaluate whether they are eligible for a discount or a senior citizen privilege using if statements.

  Tasks:

  - 1. Create three variables:
    - customer_name = "Amit"
    - customer_age = 24
    - total_purchase = 1200
  - 2. If total_purchase is greater than 1000, print "Eligible for discount".
  - 3. If customer_age is greater than or equal to 60, print "Senior Citizen"

```py
# Step 1: Define customer details
customer_name = "Amit"
customer_age = 24
total_purchase = 1200

# Step 2: Check if customer is eligible for discount (if purchase > 1000)
if total_purchase > 1000:
    print("Eligible for discount")

# Step 3: Check if customer is a senior (age >= 60)
if customer_age >= 60:
    print("Senior Citizen")
```

<br>

### 22] Building a Snack System

#### Best way to learn how to build software

- [x] A local cafe wants a program that suggests a snack. If a customer asks for cookies or samosa, it confirms the order. Otherwise, it says it's not available.

- Task:
  - Take snack input
  - It it's `"cookies"` or `"samosa"`, confirm the order
  - Else, show unavailability

#### Code breaking

- [x] Print user input

```py
snack = input("Enter your preferred snack:")

print(f"user said: {snack}")
```

- [x] User all inputs are come into a string format as all are in same lowercase

```py
snack = input("Enter your preferred snack:").lower()

print(f"user said: {snack}")
```

- [x] if, else

```py
snack = input("Enter your preferred snack:").lower()

if snack == "cookies" or snack == "samosa":
  print(f"Great Choice! We'll serve you {snack}")
else:
	print("Sorry, we only serve cookies or samsoa with tea")
```

---

> [!IMPORTANT]

### Coding Exercise

- [x] Restaurant Billing System
      You’re designing a billing system for a restaurant. Depending on the total bill amount entered by the customer, they might get a free dessert.

- Tasks:
  - 1. If the bill amount is greater than 500, return the string "You get a free dessert!"
  - 2. Otherwise, return the string: "No free dessert this time."

```py
# This function will be tested automatically.
# Do not change the function name or parameter.
def get_delivery_offer(bill_amount: float) -> str:
    # Write your code below this line
    if bill_amount > 500:
        return "You get a free dessert!"
    else:
        return "No free dessert this time."
    pass

```

<br>

### 23]

####
