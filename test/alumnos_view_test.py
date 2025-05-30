from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch, MagicMock
from types import SimpleNamespace

# Ajusta esta ruta al módulo donde esté definida tu factory para alumnos
TARGET = "alumnos.infrastructure.views_factory.Injector"


class AlumnosViewTest(APITestCase):

    @patch(TARGET)
    def test_consultar_estado_alumnos(self, mock_injector):
        # 1) Prepara un use-case falso que devuelva una lista de alumnos
        fake_uc = MagicMock()
        fake_alumnos = [
            SimpleNamespace(
                id_nfc='1234',
                nombre_completo='Daniel Martínez',
                correo_institucional='daniel@gmail.com',
                estado='Habilitado'
            ),
            SimpleNamespace(
                id_nfc='5678',
                nombre_completo='David Ochoa',
                correo_institucional='david@gmail.com',
                estado='Deshabilitado'
            )
        ]
        fake_uc.execute.return_value = fake_alumnos
        mock_injector.return_value.get.return_value = fake_uc

        # 2) Llama al endpoint
        url = '/scolaris/alumno/listar'  # Ajusta según tu configuración de rutas
        response = self.client.get(url, format='json')

        # 3) Verifica el status y el payload
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {
                'id_nfc': '1234',
                'nombre_completo': 'Daniel Martínez',
                'correo_institucional': 'daniel@gmail.com',
                'estado': 'Habilitado'
            },
            {
                'id_nfc': '5678',
                'nombre_completo': 'David Ochoa',
                'correo_institucional': 'david@gmail.com',
                'estado': 'Deshabilitado'
            }
        ])
