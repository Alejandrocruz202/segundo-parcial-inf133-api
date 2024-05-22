def render_Tarea_list(tareas):
    return [
        {
            "id": Tarea.id,
            "title":Tarea.title,
            "description":Tarea.description,
            "status":Tarea.status,
            "create_at":Tarea.create_at,
            "assigned_to":Tarea.assigned_to
        }
        for Tarea in tareas
    ]


def render_Tarea_detail(Tarea):
    return {
        "id": Tarea.id,
        "title":Tarea.title,
        "description":Tarea.description,
        "status":Tarea.status,
        "create_at":Tarea.create_at,
        "assigned_to":Tarea.assigned_to
    }
