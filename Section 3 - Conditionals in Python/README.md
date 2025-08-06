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
