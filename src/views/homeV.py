from flet import *
from components import navbar
from pages import home


class Homes(View):
    def __init__(self):
        super().__init__()
        self.route = "/"
        self.controls = [home.Home()]
        self.navigation_bar = navbar.Navv(self.change_nav)

    def change_nav(self, e):
        idx = e.control.selected_index
        match idx:
            case 0:
                self.controls = [home.Home()]
            case 1:
                self.controls = [Text("testing")]

        self.page.update()
