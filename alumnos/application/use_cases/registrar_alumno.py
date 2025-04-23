from alumnos.infrastructure.repositories import AlumnoRepositoryImpl

def registrar_alumno(data):
    repo = AlumnoRepositoryImpl()
    return repo.registrar(data)
