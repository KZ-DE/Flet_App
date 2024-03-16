from flet import *


class HomeKonten(Card):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.content = self.kontainer()

    def clicked_konten(self, e):
        print("hello")

    def kontainer(self):
        return Container(
            content=Column(
                controls=[
                    ListTile(
                        leading=Icon(icons.SETTINGS),
                        title=Text(self.title),
                        on_click=self.clicked_konten
                    )
                ]
            )
        )

    def build(self):
        return self.content
