import sqlite3
import os
import flet as ft

def connect(db_path):
    """Conecta a la base de datos y devuelve la conexión y el cursor."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn, cursor

def init_db(db_path):
    """Crea la base de datos y las tablas si no existen."""
    conn, cursor = connect(db_path)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        completed INTEGER DEFAULT 0,
        color TEXT DEFAULT '0'
    )
    """)
    conn.commit()
    conn.close()

def add_task(name, db_path):
    """Añade una nueva tarea a la base de datos."""
    conn, cursor = connect(db_path)
    cursor.execute("INSERT INTO tasks (name, completed) VALUES (?, ?)", (name, 0))
    conn.commit()
    conn.close()

def get_tasks(db_path):
    """Obtiene todas las tareas de la base de datos."""
    conn, cursor = connect(db_path)
    cursor.execute("SELECT id, name, completed, color FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id, completed, db_path):
    """Actualiza el estado de una tarea."""
    conn, cursor = connect(db_path)
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))
    conn.commit()
    conn.close()
def update_content(task_id, db_path, name):
    """Actualiza el contenido de una tarea."""
    conn, cursor = connect(db_path)
    cursor.execute("UPDATE tasks SET name = ? WHERE id = ?", (name, task_id))
    conn.commit()
    conn.close()
def update_color(task_id, db_path, color):
    """Actualiza el contenido de una tarea."""
    conn, cursor = connect(db_path)
    cursor.execute("UPDATE tasks SET color = ? WHERE id = ?", (color, task_id))
    conn.commit()
    conn.close()
def delete_task(task_id, db_path):
    """Elimina una tarea de la base de datos."""
    conn, cursor = connect(db_path)
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def count_tasks(db_path):
    """Cuenta el número de tareas pendientes."""
    conn, cursor = connect(db_path)
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed = 0")
    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_task_by_id(task_id, db_path):
    conn, cursor = connect(db_path)

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()

    conn.close()
    return task