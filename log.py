import datetime


class Log:

    @staticmethod
    def event(event: str):
        time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        formatted_event = f"{time} {event}"
        Log.__display(formatted_event)
        Log.__write_in_file(formatted_event)

    @staticmethod
    def command_event(ctx):
        command_name = ctx.invoked_with
        author = ctx.message.author
        author_nick = ctx.message.author.nick
        server = ctx.message.author.server.name
        channel = ctx.message.channel.name
        Log.event(f"Command {command_name} invoked by user: {author}({author_nick}) from server: {server}, channel: {channel}")
        
    @staticmethod
    def subcommand_event(ctx):
        subcommand_name = ctx.invoked_subcommand.name
        command_name = ctx.invoked_subcommand.parent.name
        author = ctx.message.author
        author_nick = ctx.message.author.nick
        server = ctx.message.author.server.name
        channel = ctx.message.channel.name
        Log.event(f"Subcommand {subcommand_name}({command_name}) invoked by user: {author}({author_nick}) from server: {server}, channel: {channel}")

    @staticmethod
    def __display(event: str):
        print(event)

    @staticmethod
    def __write_in_file(event: str):
        log_file = open("logs.txt", "a+")
        log_file.write(str(f"{event}\n".encode('utf8')))
        log_file.close()
