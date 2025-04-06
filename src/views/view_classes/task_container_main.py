import flet as ft
from handlers import database, cont_colors
from views import taskv
def task(tasks, db_dir, load_tasks, toggle_task, page):
    task_controls = [
            ft.Container(
                content=ft.Row([
                    ft.Checkbox(value=bool(task[2]), on_change=lambda e, t=task: toggle_task(e, t, db_dir,), active_color=cont_colors.check_color(task[3], page)),
                    ft.Text(task[1]),
                ]),
                padding=10,
                bgcolor= cont_colors.color(task[3], page),
                on_click=lambda e, t=task: taskv.view(e.page, db_dir, t, load_tasks),
                ink=True,
                border_radius=ft.border_radius.all(8),


            )
            for task in tasks
            ]

    return task_controls