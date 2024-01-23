class Square:
    """ the first methode will call in case we create an
    instance from Square it like the constructor in java
    even i didn't create it the class will call it """
    def __init__(self, size):
        """ using __ mean create it as a private access modifier """
        self.__size = size
