from django.urls import path
from .views import CursosAPIView, CursoAPIView, AvaliacoesAPIView, AvaliacaoAPIView
#Rotas locais
urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name = 'cursos'),
    path('cursos/<int:pk>', CursoAPIView.as_view(), name = 'curso'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name = 'avaliacoes'),
    path('avaliacao/<int:pk>', AvaliacaoAPIView.as_view(), name = 'avaliacao')
]