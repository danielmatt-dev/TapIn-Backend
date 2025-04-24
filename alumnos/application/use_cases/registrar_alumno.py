from alumnos.domain.ports import AlumnoRepository

def registrar_alumno(data: dict, repo: AlumnoRepository):
    return repo.registrar(data)
