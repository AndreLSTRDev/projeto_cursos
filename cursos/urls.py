from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/cadastrar/', views.cadastrar_curso, name='cadastrar_curso'),
    path('cursos/<int:curso_id>/', views.visualizar_curso, name='visualizar_curso'),
    # Defina URLs para aulas e professores seguindo o mesmo padrão
]