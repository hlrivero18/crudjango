from rest_framework import generics
from rest_framework import status
from ..models import Tarea
from ..serializer.serializer import TareaSerializer
from rest_framework.response import Response


#CRUD

#Read: solo lectura
class TareaList(generics.ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer


class TareaBuscar(generics.RetrieveAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id' #aca capturamos el parametro que sera comparada con los valores que correspondan a la clave definida

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "mensaje": "Tarea encontrada",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                "error": "No se encontró la tarea con el ID especificado"
            }, status=status.HTTP_404_NOT_FOUND)


#Create: solo creacion
class TareaCreate(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"mensaje": "Tarea creada con éxito", "data": response.data},
            status=status.HTTP_201_CREATED
        )

#UPDATE: actualizar registro por id
class TareaUpdate(generics.UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'

#DELETE: Borrar un registro por su id
class TareaDelete(generics.DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'