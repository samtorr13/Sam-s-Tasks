import sqlite3

DB_NAME = "database.db"

def connect():
    """Conecta a la base de datos y devuelve la conexión y el cursor."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    return conn, cursor

def add_task(name):
    """Añade una nueva tarea a la base de datos."""
    conn, cursor = connect()
    cursor.execute("INSERT INTO tasks (name, completed) VALUES (?, ?)", (name, 0))
    conn.commit()
    conn.close()

def get_tasks():
    """Obtiene todas las tareas de la base de datos."""
    conn, cursor = connect()
    cursor.execute("SELECT id, name, completed FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id, completed):
    """Actualiza el estado de una tarea."""
    conn, cursor = connect()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    """Elimina una tarea de la base de datos."""
    conn, cursor = connect()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def count_tasks():
    """cuenta el numero de tareas pendientes."""
    conn, cursor = connect()
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed = 0")
    count = cursor.fetchone()[0]
    conn.close()
    return count
