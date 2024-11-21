import flet as ft
from time import sleep
from datetime import datetime

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.maximized = True

    def _time():
        agora = datetime.now()

        hora = agora.strftime('%H:%M:%S')
        data = agora.strftime('%d-%m-%Y')

        return hora, data
    
    Main = ft.Card(
        width=300,
        height=300,
        elevation=5,
        color=ft.colors.BLACK,

        content=ft.Column(
            controls=[
                ft.Text(value=_time()[0], color=ft.colors.WHITE, size=20, weight='bold'),
                ft.Text(value=_time()[1], color=ft.colors.WHITE, size=20, weight='bold'),
            ],
            alignment='center',
            horizontal_alignment='center',
            spacing=0
        )
    )
    page.add(Main)

    while True:
        Main.content.controls[0].value = _time()[0]
        Main.content.controls[1].value = _time()[1]

        page.update()



if __name__ == "__main__":
    ft.app(target=main)