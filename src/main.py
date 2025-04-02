import flet as ft
from views.home import home_view

def main(page: ft.Page):
    page.title = "Task Manager"
    home_view(page)  # Cargar la vista principal

ft.app(main, view=ft.AppView.WEB_BROWSER)

