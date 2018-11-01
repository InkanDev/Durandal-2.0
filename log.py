import datetime


class Log:

    @staticmethod
    def event(event: str):
        time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        formatted_event = time + " " + event
        Log.__display(formatted_event)

    @staticmethod
    def __display(event: str):
        print(event)

    @staticmethod
    def __write_in_file(event: str):
        log_file = open("logs.txt", "a+")
        log_file.write(event + "\n")
        log_file.close()
