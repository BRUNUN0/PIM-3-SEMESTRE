import flet as ft

def main(page: ft.Page):
    # Dados para o gráfico: mês, valor percentual, cor
    dados = [
        ("Dez", 100, ft.colors.YELLOW),
        ("Nov", 90, ft.colors.GREEN),
        ("Out", 85, ft.colors.GREEN),
        ("Set", 75, ft.colors.GREEN),
        ("Ago", 65, ft.colors.BLUE),
        ("Jul", 55, ft.colors.BLUE),
        ("Jun", 45, ft.colors.BLUE),
        ("Mai", 35, ft.colors.BLUE),
        ("Abr", 25, ft.colors.RED),
        ("Mar", 20, ft.colors.RED),
        ("Fev", 15, ft.colors.RED),
        ("Jan", 10, ft.colors.RED)
    ]

    # Contêiner principal para o gráfico
    barras = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text(label, width=50),  # Label do mês
                    ft.Container(
                        width=valor * 2,  # Multiplicamos para ampliar a barra
                        height=20,
                        bgcolor=cor,
                    ),
                    ft.Text(f"{valor}%", width=40)  # Valor percentual
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10
            )
            for label, valor, cor in dados
        ],
        spacing=5
    )

    # Adicionando título e gráfico à página
    page.add(
        ft.Column(
            controls=[
                ft.Text("COLUMN DIAGRAM", size=20, weight=ft.FontWeight.BOLD),
                barras
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
