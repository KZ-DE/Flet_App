import flet as ft


class Halaman(ft.UserControl):
    def init(self):
        super().init()
        self.title = "Routes Example"

        self.views = []

        def route_change(route):
            self.views.clear()
            self.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("Flet app"),
                                  bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton(
                            "Visit Store", on_click=lambda _: self.go("/store")),
                    ],
                )
            )
            if route == "/store":
                self.views.append(
                    ft.View(
                        "/store",
                        [
                            ft.AppBar(title=ft.Text("Store"),
                                      bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.ElevatedButton(
                                "Go Home", on_click=lambda _: self.go("/")),
                        ],
                    )
                )
            self.update()

        def view_pop(view):
            self.views.pop()
            top_view = self.views[-1]
            self.go(top_view.route)

        def build(self):
            self.on_route_change = route_change
            self.on_view_pop = view_pop
            self.go(self.route)
