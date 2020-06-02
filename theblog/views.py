from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView , UpdateView      # needed for the blog
from .models import Post
from .forms import PostForm
# def blog(request):
#     return render(request, 'blog.html', {})

class BlogView(ListView):
    # to list all blogs out there
    model = Post
    template_name = 'blog.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    # Which fields you want - you take this from models.py, to put them all:
    fields = '__all__'


