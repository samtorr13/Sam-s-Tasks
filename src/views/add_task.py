import flet as ft
from handlers import database

def add_task_view(page: ft.Page, load_tasks, db_dir):
    """Vista para agregar una nueva tarea."""
    
    def go_back(e):
        if len(page.views) > 1:
            page.views.pop()
            page.update()

    def add_new_task(e):
        task_input = next((c for c in page.views[-1].controls if isinstance(c, ft.TextField)), None)
        if task_input and task_input.value.strip():
            database.add_task(task_input.value.strip(), db_dir)
            task_input.value = ""
            page.views.pop()
            load_tasks()
            page.update()

    page.views.append(ft.View(
        "/add_task",
        [
            ft.AppBar(title=ft.Text("Crear una nueva tarea"), bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST, leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=go_back)),
            ft.TextField(label="Nueva Tarea", on_submit=add_new_task),
            ft.ElevatedButton("Agregar", on_click=add_new_task, icon=ft.icons.ADD),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    ))
    page.update()
