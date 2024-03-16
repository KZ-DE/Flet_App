from flet import *
from pages import home


class Navv(NavigationBar):
    def __init__(self, page):
        super().__init__(
            destinations=[
                NavigationDestination(icon=icons.HOME, label="Home"),
                NavigationDestination(icon=icons.MENU, label="Rumus"),
                NavigationDestination(icon=icons.SETTINGS, label="Setting"),
            ],
            on_change=self.change_nav
        )
        self.page = page

    def change_nav(self, e):
        idx = e.control.selected_index
        self.page.controls.clear()

        match idx:
            case 0:
                self.page.add(home.Home())
            case 1:
                self.page.controls.append(TextButton("test"))

        self.page.update()

    def build(self):
        return self.destinations
