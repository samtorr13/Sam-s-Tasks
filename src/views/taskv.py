import flet as ft
from handlers import database, cont_colors
def view(page, db_dir, task, load_tasks):

    task_id = task[0]
    task = database.get_task_by_id(task_id, db_dir)
    if not task:
        return
    page.on_back_pressed = lambda e: go_back(e)
    def go_back(e):
        if len(page.views) > 1:
            page.views.pop()
            load_tasks()
            page.update()

    def delete_task(task_id, db_dir):
        database.delete_task(task_id, db_dir)
        go_back(None)

    def change_color(e, task_id, db_dir):
        database.update_color(task[0], db_dir, next(iter(e.control.selected), ""))
        page.update()

    page.views.append(ft.View(
        "/add_task",
        [
            ft.AppBar(title=ft.Text("Ver Tarea"), bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST, leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=go_back), actions=[ft.IconButton(ft.icons.DELETE, on_click=lambda e: delete_task(task_id, db_dir))]),
            ft.Row([
                ft.Checkbox(value=bool(task[2]), on_change=lambda e: database.update_task(task[0], int(e.control.value), db_dir), active_color=cont_colors.check_color(task[3], page)),
                ft.TextField(value=task[1],on_change=lambda e: database.update_content(task[0], db_dir, e.control.value)),]),
            ft.SegmentedButton(
                allow_empty_selection=True,
                selected={task[3]},
                segments=[
                    ft.Segment(
                        value="1",
                        label=ft.Text("Verde"),
                        icon=ft.Icon(ft.Icons.CIRCLE, color=cont_colors.color("1", page)),
                    ),
                    ft.Segment(
                        value="2",
                        label=ft.Text("Amarillo"),
                        icon=ft.Icon(ft.Icons.CIRCLE, color=cont_colors.color("2", page)),
                    ),
                    ft.Segment(
                        value="3",
                        label=ft.Text("Azul"),
                        icon=ft.Icon(ft.Icons.CIRCLE, color=cont_colors.color("3", page)),
                    ),
                ],
                on_change=lambda e: change_color(e, task[0], db_dir),
                )
            
   
            

        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    ))


    page.update()
