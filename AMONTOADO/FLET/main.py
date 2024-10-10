import flet as ft
from store import Store
from home import Home

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(route="/", controls=[Home(page)])
        )

        if page.route == "/store":
            page.views.append(
                ft.View(route="/store", controls=[Store(page)])
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)