from cleo import Command
from pyfiglet import Figlet


class AboutCommand(Command):
    name = "about"

    description = "Shows information about Open Redragon command line."

    def handle(self):
        custom_fig = Figlet(font='big')
        title = custom_fig.renderText('Open Redragon')
        self.line(
            f"""{title}\n<info>This package provides a unified command line interface to controls RGB lighting on Redragon keyboards</info>
            """
        )