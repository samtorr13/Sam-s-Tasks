import flet as ft
def color(task_col, page):
    theme = page.theme_mode
    if theme == ft.ThemeMode.DARK:
            if task_col == "1":
                return "#025033"
            elif task_col == "2":
                return "#ad841c"
            elif task_col == "3":
                return "#062a4c"
            else:
                return ft.colors.SURFACE_CONTAINER_HIGHEST
    elif theme == ft.ThemeMode.LIGHT:
            if task_col == "1":
                return ft.colors.GREEN_100
            elif task_col == "2":
                return ft.colors.YELLOW_200
            elif task_col == "3":
                return ft.colors.BLUE_100
            else:
                return ft.colors.SURFACE_CONTAINER_HIGHEST
    elif theme == ft.ThemeMode.SYSTEM:
            if task_col == "1":
                return ft.colors.GREEN_100
            elif task_col == "2":
                return ft.colors.YELLOW_200
            elif task_col == "3":
                return ft.colors.BLUE_100
            else:
                return ft.colors.SURFACE_CONTAINER_HIGHEST

def check_color(task_col, page):
    theme = page.theme_mode
    if theme == ft.ThemeMode.DARK:
            if task_col == "1":
                return ft.colors.GREEN_300
            elif task_col == "2":
                return ft.colors.YELLOW_700
            elif task_col == "3":
                return ft.colors.BLUE_300
            else:
                return ft.colors.SURFACE_CONTAINER_HIGHEST
    elif theme == ft.ThemeMode.LIGHT:
            if task_col == "1":
                return ft.colors.GREEN_500
            elif task_col == "2":
                return ft.colors.YELLOW_700
            elif task_col == "3":
                return ft.colors.BLUE_500
            else:
                return ft.colors.SURFACE_CONTAINER_HIGHEST
    elif theme == ft.ThemeMode.SYSTEM:
            if task_col == "1":
                return ft.colors.GREEN_100
            elif task_col == "2":
                return ft.colors.YELLOW_200
            elif task_col == "3":
                return ft.colors.BLUE_100
            else:
                return ft.colors.SURFACE_CONTAINER_HIGHEST