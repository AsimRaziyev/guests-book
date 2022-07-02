from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    authorName = forms.CharField(max_length=50, required=True, label='Author name')
    authorEmail = forms.EmailField(max_length=50, required=True, label='Author email')
    content = forms.CharField(max_length=3000, required=True, label='Content',
                              widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))