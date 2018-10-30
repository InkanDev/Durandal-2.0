class Log:

    def __init__(self):
        pass

    def event(self, event: str):
        self.__display(event)

    def __display(self, event: str):
        print(event)
