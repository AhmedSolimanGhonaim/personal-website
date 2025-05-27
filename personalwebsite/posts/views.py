from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Posts
from .forms import PostForm

class PostList(ListView):
    model = Posts
    template_name = "posts/post_list.html"
    context_object_name = "posts"



# def post_detail(request,id):
#     # post = Posts.objects.get(id=id)
#     post = get_object_or_404(Posts,id=id)
#     return render(request,"posts/post_detail.html",{"post":post})




class PostDetail(DetailView):
    model = Posts
    template_name = "posts/post_detail.html"
    context_object_name = "postdetail"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('post_list')
    login_url = 'login'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Posts
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('post_list')
    login_url = 'login'