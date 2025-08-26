from django import forms
from .models import Topics


class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = '__all__'  # ou especifique os campos do seu model Topics
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do tópico...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição do tópico...',
                'rows': 3
            }),
        }
        labels = {
            'name': 'Nome do Tópico',
            'description': 'Descrição',
        }
