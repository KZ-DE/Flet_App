from flet import *
from pages import home


class Navv(NavigationBar):
    def __init__(self, change_nav):
        super().__init__()
        self.destinations = [
            NavigationDestination(icon=icons.HOME, label="Home"),
            NavigationDestination(icon=icons.MENU, label="Rumus"),
            NavigationDestination(icon=icons.SETTINGS, label="Setting"),
        ]
        self.on_change = change_nav
