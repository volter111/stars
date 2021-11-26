from django import forms
from django.core.exceptions import ValidationError

from .models import *

# пример создания не связанной формы
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=255, label='URL')
#     text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Содержание')
#     is_published = forms.BooleanField(label='Опубликовано', required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label="Выберите категорию")


# пример создания связанной формы
class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Выберите категорию'

    class Meta:
        model = Celebrities
        fields = ['title', 'slug', 'text', 'photo', 'is_published', 'cat']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 15}),
        }

    # пишем свой пользовательский валидатор
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина больше 200 символов')
        return title
