from flet import *
from components import templet


class Home(UserControl):
    def __init__(self):
        super().__init__()
        self.isi_konten = [
            templet.HomeKonten(
                title="testing bikin aplikasi sendiri", src='icon.png', subtitle="aaaa",
                go='/test'
            ),
            templet.HomeKonten(
                title="testing bikin aplikasi sendiri", src='icon.png',
                go='/test2'
            ),
        ]

    def build(self):
        return ListView(
            padding=10,
            controls=[self.isi_konten[i] for i in range(len(self.isi_konten))]
        )
