from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from alumnos.infrastructure.serializers import AlumnoSerializer
from alumnos.application.use_cases.registrar_alumno import registrar_alumno

@api_view(['POST'])
def registrar_alumno_view(request):
    serializer = AlumnoSerializer(data=request.data)
    if serializer.is_valid():
        alumno = registrar_alumno(serializer.validated_data)
        return Response(AlumnoSerializer(alumno).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
