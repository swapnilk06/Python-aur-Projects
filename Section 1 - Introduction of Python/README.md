# Python - Learn by Building Projects : Section 1

## Section 1: Introduction with coding world with python

### 1] What is Programming?

- Giving instruction to a computer and the instruction which computer do understand(i.e. <b>the most important</b>).
- `Coding` is all about having the process, breaking down the stes and thinking more.
- Writing code is the easy part -> Thinking about it - `having the thought process of a programmer.` i.e. the toughest part of it.

<br>

### 2] Convert that into Python Code

- [x] **Fuction** menas => just Wrap instruction in a box

<br>

### 3] A Real World Python COde Intro

- [x] `Object`
- In the world of programming lot of things are called as **Object**

  - E.g. cup, kettle, chai

- [x] `Properties`

  - E.g. cup color, chai sweetness

- [x] `Methods/Functions`

  - E.g. actions -> stir, pour, drink

- Open up a factory, there is method knows as => `__init__`
- class init ==> means class initialize

<br>

### 4] Why do want to learn Python?

- [x] Portable
  - Once being written it can be used on anywhere at all.
- [x] Readable i.e. kind of predictable
- [x] Productive
- [x] Standard library
- [x] Multi-use

<br>

### 5] Writing first Python code

- [x] In shell running problem is `no memory` or there is no store way of keeping the files.
- [x] Test python

```bash
python testpython.py
3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)]
```

<br>

### 6] Get everything in Virtual Environment (Traditional Way)

- [x] Story behind Virtual Environment
  - Its like **safeguarding** your application from other versions & don't clutter your operating system.
  - Program actually moves safely in other environment as well on Linux, on Mac or other computer.
  - For every application create standalone Python Environment.

> 1. Create python virtual environment

```bash
	python -m venv .venv
```

- **.venv** -> dot means hidden from regular files.

> 2. Activate virtual environment (in git bash)

```bash
	source .venv/Scripts/activate
```

> 3. Install third party software or module

- Create **requirements.txt**

```bash
pip install -r requirements.txt
```

- [x] New way of virtual env installation => `UV`

<br>

### 7] Organize Python Code like a Pro

```
  chai_shop/
    run.py -> start the app
    chai.py
    processing/
    utils/
      __init__.py

```

- [x] Examples of Modules

```
  run.py -> start the app
  chai.py
```

- [x] Example of Packages
  - Any folder has \***\*init**.py\*\* empty file is called `package`

```
  utils/
    __init__.py

```

> [!NOTE]
>
> - `processing/` -> not a packages bcz, not include any **init**.py
> - It just file or folder

<br>

### 8] PEP8 & Zen of python

- [x] [PEP 8](https://peps.python.org/pep-0008/) -> Style Guide for Python Code

  - always use 4 spaces, never tabs
  - use chai, not c1

- [x] zen of python

```bash
  python
```

```bash
>>> import this
  The Zen of Python, by Tim Peters
        ...
        ...
        ...
```

<br>

--------

> [!IMPORTANT]
### Basics of Python & Programming

- [x] 1. What is programming?
  => Programming is the process of writing instructions(code) that a computer can follow to perform specific tasks.

- [x] 2. What do machines accept to perform tasks?
  => Machine don't think; they need exact instructions (in the form of code) to perform any task.

- [x] 3. What is a function in Python?
  => Function let you orgainze your code into logical blocks that can be reused, reducing repetition and improving readability.

- [x] 4. What is a class in Python?
  => A class defines how something should behave. It's a template used to create multiple similar objects.(A blueprint to create objects)

- [x] 5. What are objects?
  => Objects are specific instances of classes - like a particular car made form a car (class)blueprint. (Real-world Instances are created from classes)

- [x] 6. Functions are also called as:
  => When functions are defined inside a class and used with an object, they are called methods.

- [x] 7. Why do we use a virtual environment in Python?
  => Virtual environments let you manage dependencies separately for each project, avoiding conflicts between packages.(To isolate project dependencies)

- [x] 8. What is PEP8?
  => The official style guide for writing Python code



