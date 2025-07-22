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


