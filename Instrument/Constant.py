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

    def __str__(self):
        string = "+--------------------+\n"
        string += f"| name: {self.__name}\n"
        string += f"| type: {self.__type}\n"
        string += f"| value: {self.__value}\n"
        string += "+--------------------+\n"
        return string

