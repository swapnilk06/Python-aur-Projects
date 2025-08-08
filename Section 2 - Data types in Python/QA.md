> [!IMPORTANT]

### Quiz: Data Types in Python

1] Which of the following data types is immutable in Python?
=> "String" => Strings cannot be changed once created. List and dictionaries are mutable.

2]

3] What is the output of the following code?

```py
a = 5
b = 5
print(id(a) == id(b))
```

=> "True" => Small integers are cached in Python, so a and b point to rhe same memory location.

4] Which of the following values is NOT a valid integer in Python?
=> "2.5" => 2.5 is a float, not an integer.

5] What is the output of the following logical operation?
=> "False" => The and operator returns False if any operand is False.

6] What does this return?

```py
"Python"[0]
```

=> "P" => Indexing starts at (), so "Python"[0] returns the first character.

7] What is the output of this slice?

```py
"Programming"[0:5]
```

=> "Progr" => Slicing includes the start index (0) but excludes the stop index (5).

8] Which of the following statements is correct about string slicing?
=> "You can slice backwards using a negative step" => String slicing supports negative steps like [::-1] for reverse strings.

9] Which encoding will fail to encode the following string: "café"?
=> "ascii" => ASCII only supports characters with values 0-127. é(in "café") is not part of ASCII.

10] Which of the following is a valid tuple in Python?
=> "(1,2,3)" => Tuples are defined using parentheses ().

11] Which of these statements is not true about tuples in Python?
=> "Tuples can be changed after creation" => Tuples are immutable, s they cannot be modified after creation.

12] Which operator is used for membership testing in tuples?
=> "in" => in is the membership operator used to check if an element exists in a tuple or other collections.

13] What will this output be?

```py
t = ("apple", "banana", "cherry")
print("mango" in t)
```

=> "False" => "mango" is not in the tuple, so the result is False.

14] Which method adds an element at the end of a list?
=> "append" => append() adds a single element to the end of the list.

15] What list method can add multiple elements at once?
=> "extend" => extend() takes an iterable and appends all its elements to the list.

16] What does list.pop() do by default?
=> "Removes the last element" => Without an index, pop() removes and returns the last item in the list.

17] Which list method removes a specific value?
=> "remove" => remove() deletes rhe first occurrence of the specified value.

18] How do you insert an item at a specific index in a list?
=> "list.insert(index,item)" => insert() places the item at the given index without removing any elements.

19] What does the reverse() method do?
=> "Reverses the list in place" => reverse() modifies the original list by reverding in place.

20] Which method sorts a list in ascending order by default?
=> "sort()" => sort() the list in place in asccending order unless specified otherwise.
