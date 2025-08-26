from django import forms
from .models import Questions
from topics.models import Topics


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['statement', 'alternative_a', 'alternative_b',
                  'alternative_c', 'alternative_d', 'alternative_e']
        widgets = {
            'statement': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o enunciado da questão...',
                'rows': 4
            }),
            'alternative_a': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'alternative_b': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'alternative_c': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'alternative_d': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'alternative_e': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'statement': 'Enunciado da Questão',
            'alternative_a': 'Alternativa A (Correta)',
            'alternative_b': 'Alternativa B (Correta)',
            'alternative_c': 'Alternativa C (Correta)',
            'alternative_d': 'Alternativa D (Correta)',
            'alternative_e': 'Alternativa E (Correta)',
        }
        help_texts = {
            'statement': 'Digite o enunciado completo da questão.',
            'alternative_a': 'Marque se a alternativa A é correta.',
            'alternative_b': 'Marque se a alternativa B é correta.',
            'alternative_c': 'Marque se a alternativa C é correta.',
            'alternative_d': 'Marque se a alternativa D é correta.',
            'alternative_e': 'Marque se a alternativa E é correta.',
        }

    # Campo para selecionar tópicos (caso queira adicionar via formulário)
    topics = forms.ModelMultipleChoiceField(
        queryset=Topics.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-check-input'}),
        required=False,
        label='Tópicos relacionados',
        help_text='Selecione os tópicos relacionados a esta questão.'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se estiver editando uma questão existente, pré-selecionar os tópicos
        if self.instance and self.instance.pk:
            self.fields['topics'].initial = self.instance.topic.all()

    def save(self, commit=True):
        question = super().save(commit=commit)
        if commit:
            # Salvar os tópicos selecionados
            if 'topics' in self.cleaned_data:
                question.topic.set(self.cleaned_data['topics'])
        return question

    def clean(self):
        cleaned_data = super().clean()

        # Validação: pelo menos uma alternativa deve estar marcada como correta
        alternatives = [
            cleaned_data.get('alternative_a'),
            cleaned_data.get('alternative_b'),
            cleaned_data.get('alternative_c'),
            cleaned_data.get('alternative_d'),
            cleaned_data.get('alternative_e'),
        ]

        if not any(alternatives):
            raise forms.ValidationError(
                'Pelo menos uma alternativa deve estar marcada como correta.'
            )

        return cleaned_data
