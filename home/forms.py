from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
      text = forms.Textarea()

      class Meta:
          model = Article
          fields = '__all__'