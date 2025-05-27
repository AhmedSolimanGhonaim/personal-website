from django.shortcuts import render

# Create your views here.
from .models import Posts
from django.views.generic import ListView
class PostList(ListView):
    model = Posts
    template_name = "posts/post_list.html"
    context_object_name = "posts"
