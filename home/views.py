from django.shortcuts import render, redirect
from django.views import View
from .forms import ArticleForm
# Create your views here.

class Index(View):
    template_name='index.html'
    def get(self, request):
        form = ArticleForm()
        return render(request, self.template_name, {'form':form})