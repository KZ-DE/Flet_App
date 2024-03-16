from flet import *
from components.kontenHome import HomeKonten
from views.routers import Halaman


class Home(UserControl):
    def __init__(self):
        super().__init__()
        self.isi_konten = [
            self.konten(),
            self.konten(),
            HomeKonten("testing bikin aplikasi sendiri", 'icon.png', "aaaa"),
            HomeKonten("testing bikin aplikasi sendiri", 'icon.png'),
        ]

    def clicked_konten(self, e):
        print("Yes")
        self.page.go('/')
        self.page.update()

    def konten(self):
        return Card(
            content=Container(
                content=Column(
                    controls=[
                        ListTile(
                            leading=Icon(icons.SETTINGS),
                            title=Text("One-line selected list tile"),
                            on_click=self.clicked_konten
                        )
                    ]
                )
            )
        )

    def build(self):
        return ListView(
            padding=10,
            controls=[self.isi_konten[i] for i in range(len(self.isi_konten))]
        )
