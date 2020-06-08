

class Operand:
    __operand = None
    __size = None

    def __init__(self, operand: str):
        self.__operand = operand
        self.__size = 0
        self.__operand_processing()

    def __operand_processing(self):
        # todo: add op support
        if "[" in self.__operand:
            pass
