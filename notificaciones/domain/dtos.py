from dataclasses import dataclass

@dataclass
class NotificacionDTO:
    id_notificacion: int
    titulo: str
    descripcion: str  
    tipo: str         # "Notificación" | "Alerta"
    estado: str       # "Habilitado" | "Deshabilitado"
