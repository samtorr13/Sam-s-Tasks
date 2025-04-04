import flet as ft

def theme_change(e, page):
    theme_map = {
        "1": ft.ThemeMode.LIGHT,
        "2": ft.ThemeMode.DARK,
        "3": ft.ThemeMode.SYSTEM
    }
    page.theme_mode = theme_map.get(e.control.value, ft.ThemeMode.SYSTEM)
    page.update()