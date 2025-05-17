class Notificacion:
    def __init__(self, id_notificacion: int, titulo: str, descripcion: str, tipo: str, estado: str):
        self.id = id_notificacion
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo
        self.estado = estado
