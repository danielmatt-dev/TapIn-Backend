from datetime import date, time

from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch, MagicMock
from types import SimpleNamespace

TARGET = 'asistencia.infrastructure.views_factory.Injector'


class AsistenciaViewTests(APITestCase):

    @patch(TARGET)
    def test_consultar_por_periodo_valid_range(self, mock_injector):
        # Prepara fake use-cases
        fake_uc1 = MagicMock()
        fake_asistencias = [
            SimpleNamespace(
                id_registro_asistencia=10,
                alumno='Daniel Martínez',
                correo='daniel@gmail.com',
                grado='6',
                grupo='A',
                fecha=date(2025, 5, 15),
                hora=time(8, 0),
                tipo_registro='Normal',
                tipo_acceso='Entrada',
                estado='Habilitado'
            )
        ]
        fake_uc1.execute.return_value = fake_asistencias

        fake_uc2 = MagicMock()
        fake_alertas = [
            SimpleNamespace(
                id_alerta=1,
                titulo='Tardanza',
                descripcion='Llegó tarde',
                tipo='Tardanza'
            )
        ]
        fake_uc2.execute.return_value = fake_alertas

        # Configura el injector para devolver uc1 y uc2
        fake_inj = MagicMock()
        fake_inj.get.side_effect = [fake_uc1, fake_uc2]
        mock_injector.return_value = fake_inj

        # Llama al endpoint con parámetros válidos
        url = '/scolaris/asistencia/asistencia/periodo?fecha_inicio=2025-05-01&fecha_fin=2025-05-31'
        response = self.client.get(url, format='json')

        # Aserciones
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'asistencias': [
                {
                    'id_registro_asistencia': 10,
                    'alumno': 'Daniel Martínez',
                    'correo': 'daniel@gmail.com',
                    'grado': '6',
                    'grupo': 'A',
                    'fecha': '2025-05-15',
                    'hora': '08:00:00',
                    'tipo_registro': 'Normal',
                    'tipo_acceso': 'Entrada',
                    'estado': 'Habilitado'
                }
            ],
            'alertas': [
                {
                    'id_alerta': 1,
                    'titulo': 'Tardanza',
                    'descripcion': 'Llegó tarde',
                    'tipo': 'Tardanza'
                }
            ]
        })

    @patch(TARGET)
    def test_consultar_por_periodo_invalid_dates(self, mock_injector):
        # Injector no debería ser llamado, pero lo parcheamos para seguridad
        mock_injector.return_value = MagicMock()

        # Parámetros de fecha inválidos
        url = '/scolaris/asistencia/asistencia/periodo?fecha_inicio=not-a-date&fecha_fin=2025-05-31'
        response = self.client.get(url, format='json')

        # Aserciones para bad request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, { 'error': 'fechas inválidas' })

    @patch(TARGET)
    def test_registrar_asistencia_with_id_nfc(self, mock_injector):
        # Preparamos un use-case falso que devuelve un objeto con los atributos esperados
        fake_uc = MagicMock()
        created = SimpleNamespace(
            id_registro_asistencia=133,
            id_nfc='1234',
            correo='daniel@gmail.com',
            fecha='2025-05-30',
            hora='07:00:00',
            tipo_registro='Normal',
            tipo_acceso='Entrada',
            estado='Habilitado'
        )
        fake_uc.execute.return_value = created
        # Injector().get(...) devolverá nuestro fake_uc
        mock_injector.return_value.get.return_value = fake_uc

        url = '/scolaris/asistencia/asistencia'  # Ajusta la URL según tu enrutamiento
        payload = {
            'id_nfc': '1234',
            'fecha': '2025-05-30',
            'hora': '07:00:00',
            'tipo_registro': 'Normal',
            'tipo_acceso': 'Entrada',
            'estado': 'Habilitado'
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        print(response)

        self.assertEqual(response.data, {
            'id_registro_asistencia': 133,
            'id_nfc': '1234',
            'correo': 'daniel@gmail.com',
            'fecha': '2025-05-30',
            'hora': '07:00:00',
            'tipo_registro': 'Normal',
            'tipo_acceso': 'Entrada',
            'estado': 'Habilitado'
        })

    @patch(TARGET)
    def test_registrar_asistencia_status_400(self, mock_injector):
        # Stub del injector para que no falle al inicializar la vista
        mock_injector.return_value = MagicMock()

        url = '/scolaris/asistencia/asistencia'  # Ajusta si tu ruta es distinta
        # Payload sin 'fecha' (que es required), provocará un 400
        payload = {
            'id_nfc': '1234',
            # 'fecha'  <-- lo omitimos
            'hora': '07:00:00',
            'tipo_registro': 'Normal',
            'tipo_acceso': 'Entrada',
            'estado': 'Habilitado'
        }

        response = self.client.post(url, payload, format='json')

        # Debe ser 400 y devolver un error señalando el campo faltante
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('fecha', response.data)
        # Opcional: asegurar que el mensaje de error es del serializer
        self.assertTrue(isinstance(response.data['fecha'], list))

    @patch(TARGET)
    def test_registrar_asistencia_with_correo_only(self, mock_injector):
        fake_uc = MagicMock()
        created = SimpleNamespace(
            id_registro_asistencia=134,
            id_nfc='1234',
            correo='daniel@gmail.com',
            fecha='2025-05-30',
            hora='09:15:00',
            tipo_registro='Justificada',
            tipo_acceso='Salida',
            estado='Habilitado'
        )
        fake_uc.execute.return_value = created
        mock_injector.return_value.get.return_value = fake_uc

        url = '/scolaris/asistencia/asistencia'
        payload = {
            'correo': 'daniel@gmail.com',
            'fecha': '2025-05-30',
            'hora': '09:15:00',
            'tipo_registro': 'Justificada',
            'tipo_acceso': 'Salida',
            'estado': 'Habilitado'
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id_registro_asistencia': 134,
            'id_nfc': '1234',
            'correo': 'daniel@gmail.com',
            'fecha': '2025-05-30',
            'hora': '09:15:00',
            'tipo_registro': 'Justificada',
            'tipo_acceso': 'Salida',
            'estado': 'Habilitado'
        })
