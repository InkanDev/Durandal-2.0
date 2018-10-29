class Log:

    def __init__(self):
        pass

    def event(self, event: str):
        self.display(event)

    def display(self, event: str):
        print(event)
