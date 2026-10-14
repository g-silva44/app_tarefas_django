from django import forms
from .models import TarefaModel


class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['nome', 'descricao', 'completo', 'data_expiracao']

        widgets = {
            'data_expiracao': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                    'type': 'datetime-local',
                    'class': 'notebook-input',
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_expiracao'].input_formats = [
            '%Y-%m-%dT%H:%M',
        ]
