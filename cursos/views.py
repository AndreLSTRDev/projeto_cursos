from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Aula, Professor
from .forms import CursoForm, AulaForm, ProfessorForm
from django.contrib.auth.decorators import login_required

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})

@login_required
def cadastrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/cadastrar_curso.html', {'form': form})

def visualizar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'cursos/visualizar_curso.html', {'curso': curso})

# Crie views para aulas e professores seguindo o mesmo padrão