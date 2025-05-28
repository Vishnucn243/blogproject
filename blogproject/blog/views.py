from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from .models import Blog,Profile

# Create your views here.

class BlogListView(TemplateView):
    template_name='blog/blog.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['blogs']=Blog.objects.all().order_by('-created_at')
        return context

class BlogDetailView(DetailView):
    model=Blog
    template_name='blog/blog_detail.html'
    context_object_name='blog'

class ProfileView(TemplateView):
    template_name='blog/profile.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['profile']=Profile.objects.get_or_create(user=self.request.user)[0]
        return context

    