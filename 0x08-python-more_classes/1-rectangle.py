    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")
        if (len(position) != 2 or type(position[0]) != int or
                type(position[1]) != int or position[0] < 0 or
                position[1] < 0):
            raise Exception("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise Exception("size must be an integer")
        if value < 0:
            raise Exception("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (len(value) != 2 or type(value[0]) != int or
                type(value[1]) != int or value[0] < 0 or value[1] < 0):
            raise Exception("position must be a tuple of 2 positive integers")
        self.__position = value
