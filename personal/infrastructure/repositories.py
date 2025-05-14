from injector import inject
from personal.domain.personal import Personal
from personal.domain.ports import PersonalRepository
from personal.infrastructure.personal_model import PersonalModel
from personal.infrastructure.mapper.personal_mapper import PersonalMapper

class PersonalRepositoryImpl(PersonalRepository):

    @inject
    def __init__(self, mapper: PersonalMapper):
        self._mapper = mapper

    def registrar(self, p: Personal) -> Personal:
        model = self._mapper.to_model(p)
        model.save()
        return self._mapper.to_domain(model)

    def obtener_por_id(self, id_personal: str) -> Personal | None:
        m = PersonalModel.objects.filter(id_personal=id_personal).first()
        return self._mapper.to_domain(m) if m else None

    def eliminar(self, id_personal: str) -> bool:
        deleted, _ = PersonalModel.objects.filter(id_personal=id_personal).delete()
        return bool(deleted)

    def obtener_todos(self) -> list[Personal]:
        qs = PersonalModel.objects.all()
        return [self._mapper.to_domain(m) for m in qs]

    def actualizar(self, p: Personal) -> Personal:
        m = PersonalModel.objects.get(id_personal=p.id_personal)
        m.nombre       = p.nombre
        m.rol          = p.rol.value if hasattr(p.rol, 'value') else p.rol
        m.departamento = p.departamento
        m.correo       = p.correo
        m.estado       = p.estado
        m.save(update_fields=[
            'nombre','rol','departamento','correo','estado'
        ])
        return self._mapper.to_domain(m)
