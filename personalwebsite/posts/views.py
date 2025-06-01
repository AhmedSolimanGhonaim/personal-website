
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import Posts
from .forms import PostForm

class PostList(ListView):
    model = Posts
    template_name = "posts/post_list.html"
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Posts
    template_name = "posts/post_detail.html"
    context_object_name = "postdetail"


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Posts
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('post_list')
    login_url = 'login'
    def test_func(self):
        return self.request.user.is_superuser



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('post_list')
    login_url = 'login'
    
    def test_func(self):
        return self.request.user.is_superuser