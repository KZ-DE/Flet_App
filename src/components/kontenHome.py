from flet import *


class HomeKonten(Card):
    def __init__(self, title: str, src: str, subtitle: str | None = None,):
        super().__init__()
        self.title = title
        self.subtitle = subtitle
        self.src = src

    def clicked_konten(self, e):
        print("hello")
        # self.page.update()

    def kontainer(self):
        return Container(
            content=Column(
                controls=[
                    ListTile(
                        leading=Image(self.src, fit="contain"),
                        title=Text(self.title),
                        subtitle=Text(self.subtitle),
                        on_click=self.clicked_konten
                    )
                ]
            )
        )

    def build(self):
        self.content = self.kontainer()
        return self.content
