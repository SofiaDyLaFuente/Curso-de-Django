from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many = True)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = CursoSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        # Pode ser feito da seguinte forma também:
        # return Response("msg: criado com sucesso", status = status.HTTP_201_CREATED)
        # return Response({"id: serializer.data['id']", status = status.HTTP_201_CREATED})                   
                


class AvaliacaoAPIView(APIView):
    
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many = True)
        return Response (serializer)
    
    def put(self, request):
        serializer = AvaliacaoSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
