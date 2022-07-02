from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    authorName = forms.CharField(max_length=50, required=True, label='Имя:')
    authorEmail = forms.EmailField(max_length=50, required=True, label='Email:')
    content = forms.CharField(max_length=3000, required=True, label='Текст:',
                              widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))


class ArticleSearch(forms.Form):
    authorName = forms.CharField(max_length=50, required=True, label='Имя Автора')
