from flet import *


class K1(View):
    def __init__(self):
        super().__init__()
        self.route = "/test"
        self.controls = [
            AppBar(title=Text("Store"),
                   bgcolor=colors.SURFACE_VARIANT),
            ElevatedButton(
                "Test", on_click=self.x),
        ]

    def x(self, e):
        self.page.views.append(K2())
        # self.page.go('/test2')
        print(self.page.views)
        self.page.update()


class K2(View):
    def __init__(self):
        super().__init__()
        self.route = "/test2"
        self.controls = [
            AppBar(title=Text("K2"),
                   bgcolor=colors.SURFACE_VARIANT),
            ElevatedButton(
                "Go Home", on_click=self.x),
        ]

    def x(self, e):
        self.page.go('/')
