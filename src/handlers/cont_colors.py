import flet as ft
def color(task_col):
    if task_col == "1":
        return ft.colors.GREEN_100
    elif task_col == "2":
        return ft.colors.YELLOW_100
    elif task_col == "3":
        return ft.colors.BLUE_100
    else:
        return ft.colors.SURFACE_CONTAINER_HIGHEST