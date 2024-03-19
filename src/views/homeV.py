from flet import *
from components import navbar
from pages import home


class Homes(View):
    def __init__(self):
        super().__init__()
        self.route = "/"
        # self.controls = [home.Home()]
        self.controls = self.tab()
        self.navigation_bar = navbar.Navv(self.change_nav)

    def tab(self):
        menubar =MenuBar(
            expand=True,
            styleMenuStyle(
                alignmentalignment.top_left,
                bgcolorcolors.RED_100,
                mouse_cursor=MaterialState.HOVERED:MouseCursor.WAIT,
                            MaterialState.DEFAULT:MouseCursor.ZOOM_OUT},
            ),
            controls=[
            SubmenuButton(
                    contentText("File"),
                    on_open=handle_on_open,
                    on_close=handle_on_close,
                    on_hover=handle_on_hover,
                    controls=[
                    MenuItemButton(
                            contentText("About"),
                            leadingIconicons.INFO),
                            styleButtonStyle(
                                bgcolor=MaterialState.HOVERED:colors.GREEN_100}),
                            on_click=handle_menu_item_click
                        ),
                    MenuItemButton(
                            contentText("Save"),
                            leadingIconicons.SAVE),
                            styleButtonStyle(
                                bgcolor=MaterialState.HOVERED:colors.GREEN_100}),
                            on_click=handle_menu_item_click
                        ),
                    MenuItemButton(
                            contentText("Quit"),
                            leadingIconicons.CLOSE),
                            styleButtonStyle(
                                bgcolor=MaterialState.HOVERED:colors.GREEN_100}),
                            on_click=handle_menu_item_click
                        )
                    ]
                ),
            SubmenuButton(
                    contentText("View"),
                    on_open=handle_on_open,
                    on_close=handle_on_close,
                    on_hover=handle_on_hover,
                    controls=[
                    SubmenuButton(
                            contentText("Zoom"),
                            controls=[
                            MenuItemButton(
                                    contentText("Magnify"),
                                    leadingIconicons.ZOOM_IN),
                                    close_on_click=False,
                                    styleButtonStyle(
                                        bgcolor=MaterialState.HOVERED:colors.PURPLE_200}),
                                    on_click=handle_menu_item_click
                                ),
                            MenuItemButton(
                                    contentText("Minify"),
                                    leadingIconicons.ZOOM_OUT),
                                    close_on_click=False,
                                    styleButtonStyle(
                                        bgcolor=MaterialState.HOVERED:colors.PURPLE_200}),
                                    on_click=handle_menu_item_click
                                )
                            ]
                        )
                    ]
                ),
            ]
        )

    def change_nav(self, e):
        idx = e.control.selected_index
        match idx:
            case 0:
                self.controls = [home.Home()]
            case 1:
                self.controls = [Text("testing")]

        self.page.update()
