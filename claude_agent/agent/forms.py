from django import forms
from .models import Document, Analysis

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя документа'}),
            'file': forms.FileInput(attrs={'class': 'form-control'})
        }

class AnalysisCreateForm(forms.ModelForm):
    custom_prompt = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Введите ваш запрос для анализа документов. Например: "Сравни эти два отчета и найди несоответствия" или "Посчитай, сколько раз встречается слово «проект»"'
        }),
        help_text='Оставьте поле пустым для использования стандартного сравнительного анализа.'
    )
    
    class Meta:
        model = Analysis
        fields = ['custom_prompt'] 