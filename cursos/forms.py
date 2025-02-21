from django import forms
from .models import Curso, Aula, Professor

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'descricao_detalhada': forms.Textarea(),
            'requisitos': forms.Textarea(),
        }

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(),
        }

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(),
        }