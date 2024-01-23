# Python - Classes and Objects

In this project, we start object-oriented programming using
classes and objects in Python. I learned about attributes, methods, and
properties as well as data abstraction, data encapsulation, and information
hiding.
## abstraction :page_with_curl:
it is a methode that i can hide the implementation of the methode, class or interface and 
foucs on the logic and the functionaliy no matter what is the code inside that methode, class or interface look like 
all what we need is to employee the code to serve my goal.
## encapsulation :page_with_curl:
Because i used java before i will explain based on it in java we can use access modifiers such as
private, protected and public to annonus the definition of the variables
meaning private is only accessible within the class or method that you announce the variable as a private
protected is only accessible through the package and public is accessible through the project
so that concept we can achieve by hiding data from other classes or methode for secuirty .
## Tasks :page_with_curl:

* **0. My first square**
  * [0-square.py](./0-square.py): Python class `Square` that defines a square.

* **1. Square with size**
  * [1-square.py](./1-square.py): Python class `Square` that defines a square. Builds on
  [0-square.py](./0-square.py) with:
    * Private instance attribute `size`.
    * Instantiation with `size`.

* **2. Size validation**
  * [2-square.py](./2-square.py): Python class `Square` that defines a square. Builds on
  [1-square.py](./1-square.py) with:
    * Instantiation with optional `size`: `def __init__(self, size=0):`
  * If a provided `size` attribute is not an integer, a `TypeError` exception
  is raised with the message `must be an integer`.
  * If a provided `size` attribute is less than `0`, a `ValueError` exception
  is raised with the message `size must be >= 0`.

* **3. Area of a square**
  * [3-square.py](./3-square.py): Python class `Square` that defines a square. Builds on
  [2-square.py](./2-square.py) with:
    * Public instance attribute `def area(self):` that returns the current
    square area.

* **4. Access and update private attribute**
  * [4-square.py](./4-square.py): Python class `Square` that defines a square. Builds on
  [3-square.py](./3-square.py) with:
    * Property `def size(self):` to retrieve the private instance
    attribute `self`.
    * Property setter `def size(self, value):` to set `self`.

* **5. Printing a square**
  * [5-square.py](./5-square.py): Python class `Square` that defines a square. Builds on
  [4-square.py](./4-square.py) with:
    * Public instance method `def my_print(self):` that prints the square
    with the character `#` to standard output (if `size` == 0 -> prints an empty
    line).

* **6. Coordinates of a square**
  * [6-square.py](./6-square.py): Python class `Square` that defines a square. Builds on
  [5-square.py](./5-square.py) with:
    * Private instance attribute `position`.
    * Property `def position(self):` to retreive `position`.
    * Property setter `def position(self, value):` to set `position`.
    * Instantiation with optional `size` and `position`:
    `def __init__(self, size=0, position=(0, 0)):`
  * If a provided `position` attribute is not a tuple of two integers, a
  `TypeError` exception is raised with the message `position must be a tuple of
  2 positive integers`.

