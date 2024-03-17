from flet import *


class HomeKonten(Card):
    def __init__(self, title: str, src: str, go, subtitle: str | None = None,):
        super().__init__()
        self.title = title
        self.subtitle = subtitle
        self.src = src
        self.go = go

    def clicked_konten(self, e):
        self.page.go(self.go)

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
