# Python - Learn by Building Projects : Section 2

## Section 2: Data types in Python

### 12] Objects - Mutable and Immutable in Python

- [x] Any programming language have 2 things -
  - 1] What is `type of data`? (number,string,..)
  - 2] How do we `manipulate that data`? (add numbers, multiple numbers,...)

#### Object and Mutability

- [x] What is Object?
  - Everything is object in python
  - Every single object will have a unique id.`Identity`.
  - Every object also have a unique `Type` as well.
  - Each of object will have some of the `Value`.

#### Mutable and Immutable

- [x] Mutable -> that is `changeable`.
- [x] Immutable -> that is `NOT changeable`.

> - [!NOTE]
> - This **id(`Identity`)** helps us to figure out whether it's actually changeable or its not changeable.
> - Confirmation about wheather it's mutable or immutable with the <i>Value</i>, that is wrong way(Never do it check with value).

#### How can say that number is immuntable?

```py
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")
```

> - Never check with value.
> - Python did behind the scene for it took this new number 12 (not changing actual value 2 as 12).
> - What we changing now is `reference`.
> - Always remember what we are changing, What seen to changing in the world of mutable ==> Is the `reference`.

#### What's the proof of it?

- always check with `Identity`, never for the value.

- Track based on identity, how to find?

```py
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")

# numbers (2,12,..) are consider as -> Immutable

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")
# ID of 2: 140736940884936
# ID of 12: 140736940885256
```

- Both **ID's are totally different** i.e. Immutable -> that is `NOT changeable`.

#### Things of mutable

```py
spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
spice_mix.add("Ginger")
spice_mix.add("Cardamom")
print(f"After spice mix id: {id(spice_mix)}")
# Initial spice mix id: 2347941561056
# After spice mix id: 2347941561056
```

- Both **ID's are same** i.e. Mutable -> that is `Changeable`.

> - [!IMPORTANT]
> - Whole concept of **Mutable** & **Immutable** is `what value can I change?` & what values I cannot change in the memory itself.
>   - `Numbers are immutable` -> this simply means I cannot change this number's existence in the memory.
>     - I can change the reference where I'am pointing, but nothing can actually be changed. => `Immutable`.
> - Same object can be changed (in set() example) still id remain exactly same => `Mutable`.

<br>

### 13] Numbers, Booleans and Operators in Depth in Python

#### Types of Numbers

- Integers
- Boolean
- Real Number
  - Floating -> decimal
- Complex Number e.g. 2 + 3j

- [x] Boolean Logical operation -> and, or, not
- 1] tea or coffee -> "any one can be true"
- 2] tea and coffee -> "both should be true"
- 3] not -> opposite

---

> [!IMPORTANT]

### Coding Exercise

- [x] Playing with Numbers
      Write a Python program that performs the following operations and prints the results
  - Addition
  - Subtraction
  - Multiplication
  - Division (float result)
  - Floor Division (integer result)
  - Modulus (remainder)

```py
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # Floor Division (integer result)
print(a%b)  # Modulus (remainder)
```

<br>

### 14] String - Index, Slice and Encoding

- [x] Best time to learn the string is when build something, do some projects in it.

#### String - core, indexing, slicing, Encoding-Decoding

> [!NOTE]
>
> - String is `Immutable` -> **They cannot be changed**
> - In the memory always actually `create a new referenece`.

#### How do we use the string?

```py
chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")
```

- [x] `Indexing` => means each letter in this string is represented by a number.

#### Last number is not inclusive in the world of python

- [x] Without including 'c' in => 0 to 7 indexing

```py
chai_description = "Aromatic and Bold"

print(f"First Word: {chai_description[0:7]}")
```

=> First word: Aromati

- [x] We want to C as well

```py
chai_description = "Aromatic and Bold"

print(f"First Word: {chai_description[0:8]}")
```

=> First word: Aromatic

---

> [!IMPORTANT]

### Coding Exercise

- [x] Should You Go for a Walk?
      You’re deciding whether to go for a walk based on two real-life conditions:

  - is_sunny = True
  - have_umbrella = False

  Print the result of the following:

  - Is it not sunny today?
  - Do you not have an umbrella?
  - Should you go for a walk if it’s sunny and you don’t need an umbrella?
  - Should you go for a walk if it’s sunny or if you have an umbrella?

```py

is_sunny = True
have_umbrella = False

print(not is_sunny)
print(not have_umbrella)
print(is_sunny and not have_umbrella)
print(is_sunny or have_umbrella)

```

<br>

### 15] Tuples and Membership Testing

#### What are the Tuples?

- Tuples --> `()` => `Parenthesis`
- Tuples are `Immutable` => **They are can't be change**.
- Python dosn't need third variable for swapping two
  values.
- Tuples are "Case Sensitive"
  - cinnamon & Cinnamon -> are differents
  ```py
  print(f"Is ginger in masala spices: {'cinnamon' in masala_spices}")
  print(f"Is ginger in masala spices: {'Cinnamon' in masala_spices}")
  ```
- `Membership testing or membership test` => You need to ask that what you are looking for in the tuple as availability.
  -Whole thing depends on this keyword which is -> `in`

> [!NOTE]
>
> - `()` => `Parenthesis`
> - `[]` => `Brackets`
> - `{}` => `Curly braces or Braces`

---

> [!IMPORTANT]

### Coding Exercise

- [x] Swapping Temperature

  - You are building a temperature converter app. Sometimes, due to incorrect input order, the min_temp and max_temp values are swapped.

  - Current values are

    - min_temp = 40
    - max_temp = 25

  - Use Python tuples to swap them back to the correct order.

```py
min_temp = 40
max_temp = 25

min_temp, max_temp = max_temp, min_temp

print(min_temp)
print(max_temp)
```

=> 25
40

<br>

### 16] Basic of List in python

> [!IMPORTANT]
>
> - `Immutable` -> They cannot be changed -> `Once the memory reference is done`, that is means it cannot be changed.
>   - It get a unique id, that unique ID never changes that.
> - `Mutable` -> They can be changed
>   - There can be append method, insert method... just becz, they are mutable.

#### Mutable DataType - **List**

- [x] `List` _(In world of python it called only list)_
  - In other programing language it called as `Array`.
  - There is no difference between in **List & Array**

#### Position in list

```bash
Chai: ['water', 'milk', 'ginger', 'cardamom']
```

- 0th => water
- 1st => milk
- 2nd => ginger
- 3rd => cardamom

- [x] `appends` -> always adds it at the very end of list.
- [x] `insert` -> provide what position you want to add.
  - This position known as `index`

#### Other methods in list mostly used

- [x] `extend` -> always add the elements at the end.
- [x] `pop` -> always remove the last element.
- [x] `Reverse` -> each postion will be reversed.
- [x] `Sort` -> each postion will be sorted.

<br>

### 17] Operator overloading and bytearray in python

#### Operator Overloading

- There are a lot of operators in the world of programming like `+`
- `+` plus is an operator which can adds two things, which are **left and right** e.g. 2 + 3 => This is designed to add numbers.
- But whenever this operator whatever it is, it's being used for `doing more than one task` that is called as **Operator Overloading**.

#### Operator Overloading in list

```py
strong_brew = ["black tea"] * 3
print(f"Strong brew: {strong_brew}")
```

#### Bytearray

- I want juat one string "CINNAMON"
- How we can do that? => `bytearray` => in this used method => `()` also tuples as well as for method

```py
# It used rarely but its exists
raw_spice_data = bytearray(b"CINNAMON") # each element will be treated as array
print(f"Bytes: {raw_spice_data}")
```

- [x] Advantages of this
- You can actually perform **all these replace** and **all these things**.

- Output not proper of bytearray

```py
raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}") # Investigation study to fix
```

- Innvestigation study can fix this output

```py
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")
```

---

> [!IMPORTANT]

### Coding Exercise

Shopping List
You’re building a shopping list feature in a grocery app. You need to support various list operations such as adding items, removing them, merging with others, and handling user inputs from text.

Tasks:
1] Create a grocery list named my_cart with the items: "apples", "bananas", and "milk"
Print the grocery list.

2] Add "bread" to the end of the list.
Print the updated grocery list.

3] Insert "ketchup" at the beginning of the list.
Print the updated grocery list.

4] Remove "bananas" from the list.
Print the updated grocery list.

5] Remove the last item from the list and store it in a variable named removed_item.
Print the value of removed_item.

6] Extend the grocery list by adding "rice" and "butter".
Print the updated grocery list.

7] Sort the grocery list in alphabetical order.
Print the updated grocery list.

8] Reverse the order of the grocery list.
Print the updated grocery list.

9] Concatenate the grocery list with another list containing "juice" and "jam".
Print the resulting list.

10] Duplicate the grocery list twice.
Print the resulting list.

11] Define a string with the value "tomato cucumber spinach" and convert it into a list.
Print the converted list.

```py

my_cart = ["apples", "bananas", "milk"]
print(f"{my_cart}") # ['apples', 'bananas', 'milk']

# Append
my_cart.append("bread")
print(f"{my_cart}") # ['apples', 'bananas', 'milk', 'bread']

# Insert
my_cart.insert(0,"ketchup")
print(f"{my_cart}") # ['ketchup', 'apples', 'bananas', 'milk', 'bread']

# Remove
my_cart.remove("bananas")
print(f"{my_cart}") # ['ketchup', 'apples', 'milk', 'bread']

# Pop - Remove last
removed_item = my_cart.pop()
print(f"{removed_item}") # bread

# Extend
my_cart.extend(["rice", "butter"])
print(f"{my_cart}") # ['ketchup', 'apples', 'milk', 'rice', 'butter']

# Sort
my_cart.sort()
print(f"{my_cart}") # ['apples', 'butter', 'ketchup', 'milk', 'rice']

# Reverse
my_cart.reverse()
print(f"{my_cart}") # ['rice', 'milk', 'ketchup', 'butter', 'apples']

# Concatenate
new_items = ["juice", "jam"]
resulting_list = my_cart + new_items
print(f"{resulting_list}") # ['rice', 'milk', 'ketchup', 'butter', 'apples', 'juice', 'jam']

# Duplicate
resulting_list = my_cart * 2
print(f"{resulting_list}") # ['rice', 'milk', 'ketchup', 'butter', 'apples', 'rice', 'milk', 'ketchup', 'butter', 'apples']

# String to list
v_string = "tomato cucumber spinach"
v_list = v_string.split()
print(f"{v_list}") # ['tomato', 'cucumber', 'spinach']

```

<br>

### 18] Set and frozenset in python

#### Sets => `{}`

- sets are super easy in python
- `Union` => `|` => "pipe operator"
  - Get all of them, but "don't get the reputation".
  - It's a "very unique property" of this.
- `Intersection` => `&` => "And operator"
  - Only that "which is common between both of them".
  - Would be no common, we get nothing.
- `Differences` => `-`

  - Ignoreing the common form 1st viceversa.

- [x] Membership test

```py
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")
```

=> True # whenever clove present in optinal*spices otherwise \_False*

#### Frozenset

- If you want to "freeze any of the set" there is a concept known as `frozen set`.
- It's an "immutable unordered collection of unique elements".

> [!NOTE]
>
> - `Set` by default is known for uniqueness only.
> - Working wise of `Set` & `Frozenset` are exactly same.


---

> [!IMPORTANT]

### Coding Exercise

Managing Store Inventory
  You’re managing product categories for a retail store. Your task is to identify:
  - Which products are available in which branches
  - What products are common
  - What products are missing in each branch
  - And which products should not be altered using frozenset

Tasks:
1] Create a set branch_a_products with the items: "bread", "milk", "butter", "jam". Create another set branch_b_products with the items: "bread", "cheese", "butter", "ketchup". Print both sets.
2] Find and print the union of both branches’ products.
3] Find and print the intersection of both branches’ products.
4] Find and print the products that are in branch_a_products but not in branch_b_products.
5] Check whether "ketchup" is available in branch_a_products and print the result.
6] Define a frozenset called essential_items with values: "milk", "bread", "ketchup". Print the frozenset.

```py

branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}

print(branch_a_products) # {'milk', 'bread', 'jam', 'butter'}
print(branch_b_products) # {'bread', 'cheese', 'ketchup', 'butter'}

# union
print(branch_a_products | branch_b_products) # {'milk', 'bread', 'jam', 'ketchup', 'butter', 'cheese'}

# intersection
print(branch_a_products & branch_b_products) # {'bread', 'butter'}

# difference 
print(branch_a_products - branch_b_products) # {'milk', 'jam'}

# Membership test
print('ketchup' in branch_a_products) # False

# frozenset - Immutable - not be change
essential_items = frozenset(["milk","bread","ketchup"])
print(essential_items) # 
frozenset({'milk', 'bread', 'ketchup'})

```

<br>

### 19] 

#### 