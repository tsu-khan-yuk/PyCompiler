from PyCompiler.Instrument.Database import constant_type


class Constant:
    __name = None
    __type = None
    __value = None
    __size = None

    def __init__(self, string: str):
        string = string.split()
        self.__name = string[0]
        self.__type = string[1]
        self.__value = string[2]
        self.__size = 0
        self.__const_processing()

    def __const_processing(self) -> None:
        if '"' not in self.__value:
            self.__size = len(self.__value[1:-1]) * constant_type[self.__type]
        else:
            self.__size = constant_type[self.__type]

    @property
    def size(self):
        return self.__size

    def __str__(self):
        string = "+--------------------+\n"
        string += f"| name: {self.__name}\n"
        string += f"| type: {self.__type}\n"
        string += f"| size: {self.__size}\n"
        string += f"| value: {self.__value}\n"
        string += "+--------------------+"
        return string
