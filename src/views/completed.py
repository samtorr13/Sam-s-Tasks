import flet as ft
from handlers import database, nav_hand
from views.add_task import add_task_view

def completed_view(page: ft.Page):
    """Vista principal con la lista de tareas."""
    
    def load_tasks():
        page.views.clear()
        pending_tasks_count = database.count_tasks()
        tasks = database.get_tasks()

        tasks = [task for task in tasks if task[2] == 1]

        task_controls = [
            ft.Row([
                ft.Checkbox(label=task[1], value=bool(task[2]), on_change=lambda e, t=task: toggle_task(e, t)),
                ft.IconButton(ft.icons.DELETE, on_click=lambda e, t=task: remove_task(t))
            ])
            for task in tasks
        ]

        page.views.append(ft.View(
            "/",
            [
                ft.AppBar(title=ft.Text("Tareas Completadas"), bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST),
                *task_controls,
            ],
            floating_action_button=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=lambda e: add_task_view(page, load_tasks)),
            navigation_bar=ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
                    ft.NavigationBarDestination(icon=ft.Icons.CHECK_BOX, label="Tareas Completadas"),
                ], on_change=lambda e: nav_hand.nav(page, e.control.selected_index), selected_index=1
            )
        ))
        page.update()

    def toggle_task(e, task):
        database.update_task(task[0], int(e.control.value))
        load_tasks()

    def remove_task(task):
        database.delete_task(task[0])
        load_tasks()

    load_tasks()