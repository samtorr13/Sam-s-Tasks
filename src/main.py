import flet as ft
from views.home import home_view

def main(page: ft.Page):
    page.title = "Task Manager"
    theme = page.client_storage.get("theme")
    if theme == "1":
        page.theme_mode = ft.ThemeMode.LIGHT
        page.bgcolor = ft.colors.WHITE
    elif theme == "2":
        page.theme_mode = ft.ThemeMode.DARK
        page.bgcolor = ft.colors.BLACK
    elif theme == "3":
        page.theme_mode = ft.ThemeMode.SYSTEM
        page.bgcolor = ft.colors.SURFACE_CONTAINER_HIGHEST
    home_view(page)  # Cargar la vista principal

ft.app(main)

