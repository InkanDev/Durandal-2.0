import datetime


class Log:

    def __init__(self):
        pass

    def event(self, event: str):
        time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        formatted_event = time + " " + event
        self.__display(formatted_event)

    def __display(self, event: str):
        print(event)

    def __write_in_file(self, event: str):
        log_file = open("logs.txt", "a+")
        log_file.write(event + "\n")
        log_file.close()

