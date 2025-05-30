from typing import List, Dict

from injector import Injector

from alertas.domain.alerta import Alerta
from alumnos.domain.alumno import Alumno
from alumnos.domain.ports import AlumnoRepository
from asistencia.domain.dtos import AsistenciaResponse
from inscripciones.infrastructure.injector_modules import InscripcionesInjectorModule


class GenerarAlertas:

    def execute(self, asistencias: List[AsistenciaResponse]) -> List[Alerta]:

        inj = Injector([InscripcionesInjectorModule])
        alumnos = inj.get(AlumnoRepository).obtener_todos()

        alumnos_map: Dict[str, Alumno] = {
            a.correo_institucional: a
            for a in alumnos
            if a.estado.lower() == 'activo' and not a.es_silenciado
        }

        falta_threshold = 3
        alertas: List[Alerta] = []
        faltas_contador: Dict[str, int] = {email: 0 for email in alumnos_map}
        next_id = 1

        # Procesa cada asistencia
        for a in asistencias:
            alumno = alumnos_map.get(a.correo)
            if not alumno:
                continue  # ignora registros de alumnos inactivos o no listados

            # Tardanzas
            if a.tipo_registro == 'Tardío':
                alertas.append(Alerta(
                    id_alerta=next_id,
                    titulo='Tardanza',
                    descripcion=f'El alumno {alumno.nombre_completo} llegó tarde a las {a.hora}.',
                    tipo='Tardanza'
                ))
                next_id += 1

            # Registros extraordinarios
            if a.tipo_registro == 'Extraordinario':
                alertas.append(Alerta(
                    id_alerta=next_id,
                    titulo='Registro Extraordinario',
                    descripcion=f'El alumno {alumno.nombre_completo} realizó un registro extraordinario.',
                    tipo='Extraordinario'
                ))
                next_id += 1

            # Accesos denegados
            if a.estado == 'Deshabilitado':
                alertas.append(Alerta(
                    id_alerta=next_id,
                    titulo='Acceso Denegado',
                    descripcion=f'El acceso de {alumno.nombre_completo} fue denegado.',
                    tipo='AccesoDenegado'
                ))
                next_id += 1

            # Cuenta faltas implícitas (si no existe registro de entrada)
            if a.tipo_registro not in ('Normal', 'Justificada', 'Tardío', 'Extraordinario'):
                faltas_contador[a.correo] += 1

        # Detecta faltas explícitas: alumnos sin ninguna asistencia
        asistidos = {a.correo for a in asistencias}
        for correo, alum in alumnos_map.items():
            if correo not in asistidos:
                alertas.append(Alerta(
                    id_alerta=next_id,
                    titulo='Falta',
                    descripcion=f'El alumno {alum.nombre_completo} no registró asistencia hoy.',
                    tipo='Falta'
                ))
                next_id += 1

        # Faltas recurrentes
        for correo, count in faltas_contador.items():
            if count >= falta_threshold:
                alum = alumnos_map[correo]
                alertas.append(Alerta(
                    id_alerta=next_id,
                    titulo='Faltas Recurrentes',
                    descripcion=(
                        f'El alumno {alum.nombre_completo} acumula {count} '
                        f'faltas, superando el umbral de {falta_threshold}.'
                    ),
                    tipo='FaltasRecurrentes'
                ))
                next_id += 1

        return alertas
