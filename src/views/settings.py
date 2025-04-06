import flet as ft
from handlers import database, nav_hand, settings
import os

def settings_view(page: ft.Page):

    app_dir = os.getenv('FLET_APP_STORAGE_DATA')
    theme = page.client_storage.get("theme")
    page.views.clear()#limpia la vista antes de agregar cualquier dato
    #define la vista principal
    page.views.append(ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Ajustes"), bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST),

            ft.Text("Tema", theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
            ft.SegmentedButton(
            on_change = lambda e: settings.theme_change(e, page),
            #selected_icon=ft.Icon(ft.Icons.ONETWOTHREE),
            selected={theme} if theme else {3},
            #allow_multiple_selection=True,
            segments=[
                ft.Segment(
                    value="1",
                    label=ft.Text("Claro"),
                    icon=ft.Icon(ft.Icons.LIGHT_MODE),
                ),
                ft.Segment(
                    value="2",
                    label=ft.Text("Oscuro"),
                    icon=ft.Icon(ft.Icons.DARK_MODE),
                ),
                ft.Segment(
                    value="3",
                    label=ft.Text("Auto."),
                    icon=ft.Icon(ft.Icons.BRIGHTNESS_AUTO),
                    disabled=True,
                ),
            ],
        )
        ],
        navigation_bar=ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.CHECK_BOX, label="Completadas"),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Configuración"),
            ], on_change=lambda e: nav_hand.nav(page, e.control.selected_index), selected_index=2
        )
    ))
    page.update()