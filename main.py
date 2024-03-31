import flet as ft
import dotenv as dv
import os

dv.load_dotenv()
url = os.getenv("TAXOMETERAPIURL")


def main(page: ft.Page):
    page.adaptive = True
    page.appbar = ft.AppBar(title=ft.Text(value="Taxometer"))
    body = ft.SafeArea(ft.Text("Hello, Flet!"))
    page.add(body)


ft.app(main)
