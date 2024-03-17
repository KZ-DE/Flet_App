from flet import *
from views import homeV, konten

data = {
    '/test': konten.K1(),
    '/test2': konten.K2()
}


def main(page: Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(homeV.Homes())
        if page.route != "/":
            page.views.append(data[page.route])
        page.update()
        print(f"views = {page.views} page route = {page.route}")

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


app(target=main)
