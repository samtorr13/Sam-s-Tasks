import flet as ft
import database  # Importamos la base de datos

def main(page: ft.Page):
    page.title = "Task Manager"
    pending_tasks_count = database.count_tasks()
    def load_tasks():
        """Carga las tareas desde la base de datos y las muestra en la UI."""
        page.views.clear()
        tasks = database.get_tasks()
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
                ft.AppBar(title=ft.Text(f"{pending_tasks_count} Tareas Pendientes"), bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST),
                ft.TextField(label="Nueva Tarea", on_submit=add_new_task),
                ft.ElevatedButton("Agregar", on_click=add_new_task),
                *task_controls,
            ],
        ))
        page.update()

    def add_new_task(e):
        """Añade una nueva tarea desde la UI."""
        task_input = next((c for c in page.views[0].controls if isinstance(c, ft.TextField)), None)

        if task_input and task_input.value.strip():
            database.add_task(task_input.value.strip())
            task_input.value = ""  # Limpiar el campo después de agregar la tarea
            load_tasks()


    def toggle_task(e, task):
        """Cambia el estado de una tarea (completado/no completado)."""
        database.update_task(task[0], int(e.control.value))
        load_tasks()

    def remove_task(task):
        """Elimina una tarea."""
        database.delete_task(task[0])
        load_tasks()

    # Cargar las tareas al iniciar la app
    load_tasks()

ft.app(main, view=ft.AppView.WEB_BROWSER)
