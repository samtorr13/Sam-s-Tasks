import flet as ft

def theme_change(e, page):

    theme = next(iter(e.control.selected), None)
    if theme == "1":
        page.theme_mode = ft.ThemeMode.LIGHT
        page.bgcolor = ft.colors.WHITE
    elif theme == "2":
        page.theme_mode = ft.ThemeMode.DARK
        page.bgcolor = ft.colors.BLACK
    elif theme == "3":
        page.theme_mode = ft.ThemeMode.SYSTEM
        page.bgcolor = ft.colors.SURFACE_CONTAINER_HIGHEST
    page.update()
    page.client_storage.set("theme", theme)