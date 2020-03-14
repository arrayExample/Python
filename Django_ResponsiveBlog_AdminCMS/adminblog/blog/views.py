from django.views.generic import ListView, DetailView
from .models import *


class homepage(ListView):
    template_name = 'homepage.html'
    model = homepageMessage

    def get_context_data(self, **kwargs):
        context = super(homepage, self).get_context_data(**kwargs)
        return context


class blogView(ListView):
    template_name = 'blog.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(blogView, self).get_context_data(**kwargs)
        return context


class blogdetail(DetailView):
    template_name = 'blogdetail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(blogdetail, self).get_context_data(**kwargs)
        return context
