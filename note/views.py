from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,UpdateView
from note.forms import PostForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from note.models import Post
from django.utils.decorators import  method_decorator
# Create your views here.


class PostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "home.html"
    success_url = reverse_lazy("note-post")
    def form_valid(self, form):
        form.instance.author=self.request.user
        messages.success(self.request,"post has been saved")
        self.object = form.save()
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data()
    #     blogs=Post.objects.all().order_by("-posted_date")
    #     context["blogs"]=blogs
    #     comment_form=()
    #     context["comment_form"]=comment_form
    #     return context

class PostListView(View):
    def get(self,request,*args,**kwargs):
        qs=Post.objects.all()
        return render(request, "list.html", {"post": qs})

class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "update.html"
    success_url = reverse_lazy("note-list")
    pk_url_kwarg = "emp_id"

def removeview(request,*args,**kwargs):
    id=kwargs.get("emp_id")
    phone = Post.objects.get(id=id)
    phone.delete()
    messages.success(request,"successfully deleted")
    return redirect("note-list")