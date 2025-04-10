import flet as ft
from handlers import database, nav_hand, cont_colors
from views import add_task, taskv
from views.view_classes import task_container_main as task_cont
import os

def home_view(page: ft.Page):
    
    def load_tasks(): #vista principal
        
        app_dir = os.getenv('FLET_APP_STORAGE_DATA')
        db_dir = os.path.join(app_dir, 'tasks.db')
        database.init_db(db_dir)
        page.views.clear()#limpia la vista antes de agregar cualquier dato

        pending_tasks_count = database.count_tasks(db_dir) #cuenta las tareas pendientes para mostar en el encabezado
        tasks = database.get_tasks(db_dir) #obtiene las tareas
        tasks = [task for task in tasks if task[2] == 0]
        
        #controles para cada tarea
        task_controls = task_cont.task(tasks, db_dir, load_tasks, toggle_task, page)


        #define la vista principal
        page.views.append(ft.View(
            "/",
            [
                ft.AppBar(title=ft.Text(f"{pending_tasks_count} Tareas Pendientes"), bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST, actions=[ft.IconButton(ft.icons.SEARCH,disabled=True)]),
                *task_controls,
            ],
            floating_action_button=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=lambda e: add_task.view(e.page, load_tasks, db_dir)),
            navigation_bar=ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
                    ft.NavigationBarDestination(icon=ft.Icons.CHECK_BOX, label="Completadas"),
                    ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Configuración"),
                ], on_change=lambda e: nav_hand.nav(page, e.control.selected_index)
            )
        ))
        page.update()


    #acciones de las tareas
    def toggle_task(e, task, db_dir):
        database.update_task(task[0], int(e.control.value), db_dir)
        load_tasks()

    def remove_task(task, db_dir):
        database.delete_task(task[0], db_dir)
        load_tasks()

    def task_view(page):
        taskv.view(page)
    load_tasks()
