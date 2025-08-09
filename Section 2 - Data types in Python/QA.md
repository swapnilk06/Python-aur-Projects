> [!IMPORTANT]

### Quiz: Data Types in Python

1] Which of the following data types is immutable in Python?
=> `String` => Strings cannot be changed once created. List and dictionaries are mutable.

2] What does the id() function return in Python..?
=> `Memory address of the object` => id() returns a unique identifier for the object, which is its memory address.

3] What is the output of the following code?

```py
a = 5
b = 5
print(id(a) == id(b))
```

=> `True` => Small integers are cached in Python, so a and b point to the same memory location.

4] Which of the following values is NOT a valid integer in Python?
=> `2.5` => 2.5 is a float, not an integer.

5] What is the output of the following logical operation?
=> `False` => The and operator returns False if any operand is False.

6] What does this return?

```py
"Python"[0]
```

=> `P` => Indexing starts at (), so "Python"[0] returns the first character.

7] What is the output of this slice?

```py
"Programming"[0:5]
```

=> `Progr` => Slicing includes the start index (0) but excludes the stop index (5).

8] Which of the following statements is correct about string slicing?
=> `You can slice backwards using a negative step` => String slicing supports negative steps like [::-1] for reverse strings.

9] Which encoding will fail to encode the following string: "café"?
=> `ascii` => ASCII only supports characters with values 0-127. é(in "café") is not part of ASCII.

10] Which of the following is a valid tuple in Python?
=> `(1,2,3)` => Tuples are defined using parentheses ().

11] Which of these statements is not true about tuples in Python?
=> `Tuples can be changed after creation` => Tuples are immutable, s they cannot be modified after creation.

12] Which operator is used for membership testing in tuples?
=> `in` => in is the membership operator used to check if an element exists in a tuple or other collections.

13] What will this output be?

```py
t = ("apple", "banana", "cherry")
print("mango" in t)
```

=> `False` => "mango" is not in the tuple, so the result is False.

14] Which method adds an element at the end of a list?
=> `append` => append() adds a single element to the end of the list.

15] What list method can add multiple elements at once?
=> `extend` => extend() takes an iterable and appends all its elements to the list.

16] What does list.pop() do by default?
=> `Removes the last element` => Without an index, pop() removes and returns the last item in the list.

17] Which list method removes a specific value?
=> `remove` => remove() deletes rhe first occurrence of the specified value.

18] How do you insert an item at a specific index in a list?
=> `list.insert(index,item)` => insert() places the item at the given index without removing any elements.

19] What does the reverse() method do?
=> `Reverses the list in place` => reverse() modifies the original list by reverding in place.

20] Which method sorts a list in ascending order by default?
=> `sort()` => sort() the list in place in asccending order unless specified otherwise.

21] What does max([1, 5, 3]) return?
=> `5` => max() returns the largest item in the list.

22] What is the output of min(["z", "a", "m"])?
=> `a` => min() returns the smallest item based on ASCII/lexicographic order.

23] What does "hello" + "world" return in Python?
=> `helloworld` => The + operator is overloaded for strings to concatenate them.

24] Which operator is overloaded in the expression [1, 2] + [3, 4]?
=> `+` => The + operator is overloaded to concatenate two lists into one.

25] What is the result of list("abc")?
=> `['a','b','c']` => The list() constructor converts a string into a list of characters.

26] Which of the following is a valid set in Python?
=> `{1,2,3}` => Set are design using braces {}.

27] Which method returns a set containing all unique elements from two sets?
=> `unions` => union() combines elements from both sets, removing duplicates.

28] Which method returns elements present in one set but not in the other?
=> `difference()` => set1.difference(set2) returns a set with elements only in the first set, excluding those in the second.

29] Which method returns only the common elements between two sets?
=> `intersection()` => intersection() returns a new set with elements found in both sets.

30] What will the expression "apple" in {"apple", "banana"} return?
=> `True` => The in operator checks for membership and returns True if the element exist in the set.

31] What is a key difference between set and frozenset in Python?
=> `frozenset is immutable` => Unlike set, a frozenset cannot be changed after creation.

32] Which of operations is not allowed on a frozenset?
=> `add` => frozenset is immutable, so you cannot use methods like add() or remove() on it.

33] How do you create an empty dictionary in Python?
=> `dict={}` => Curly braces {} create an empty dictonary in python.

34] Which syntax correctly adds a new key-value pair to a dictionary?
=> `dict["name"]="Alice"` => The correct way to add/update a value is using square brackets and assignment.

35] How do you access the value of the "age" key in the "person" dictionary?
=> `person["age"]` => Accessing values in a dictionary is done via dict[key].

36] Which method safely accesses a key and avoids errors if the key is missing in a dictionary?
=> `person.get("age")` => get() returns None if the key doesn't exist, preventing a keyError.

37] How do you delete a key "email" from a dictionary user?
=> `del user["email"]` => del removes a key-value pair from the dictonary.

38] Which method removes and returns the last inserted key-value pair from a dictionary?
=> `popitem()` => popitem() removes the last inserted item in Python 3.7+

39] Which method merges another dictionary into the current one?
=> `update()` => update() add key-value pairs form another dictonary to the current one.

40] What does the keys() method return?
=> `A view object of all keys` => keys() returns a dynamic view of dictionary keys.

41] Which method returns all the values in a dictionary?
=> `values()` => values returns a view object of all values in the dictionary.

42] What does the items() method return in a dictionary?
=> `A view object of (key, value) pairs` => items returns key-value pairs as tuples in a view object.

43] What is the result of "name" in person if person is a dictionary?
=> `Checks if "name" is a key` => Membership testing in dictionaries checks for keys, not values.
