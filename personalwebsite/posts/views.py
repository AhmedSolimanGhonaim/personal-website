from django.shortcuts import render , get_object_or_404



from .models import Posts
from django.views.generic import ListView , DetailView 

class PostList(ListView):
    model = Posts
    template_name = "posts/post_list.html"
    context_object_name = "posts"



# def post_detail(request,id):
#     # post = Posts.objects.get(id=id)
#     post = get_object_or_404(Posts,id=id)
#     return render(request,"posts/post_detail.html",{"post":post})




class PostDetail(DetailView):
    model =Posts
    template_name = "posts/post_detail.html"
    context_object_name = "postdetail"