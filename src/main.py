from flet import *
from components import navbar
from pages import home


def main(page: Page):
    # konfigurasi
    page.title = "My App"
    page.theme_mode = ThemeMode.SYSTEM
    page.padding = 0
    page.scroll = ScrollMode.HIDDEN

    # navbar
    page.navigation_bar = navbar.Navv(page)

    # main page
    page.add(home.Home())

    # update
    page.update()


app(main)
