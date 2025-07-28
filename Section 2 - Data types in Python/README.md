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


```

<br>

### 16] 