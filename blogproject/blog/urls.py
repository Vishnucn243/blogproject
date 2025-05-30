from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('category/<slug:slug>/', views.CategoryBlogListView.as_view(), name='category_blogs'),
    path('create/', views.CreateBlogView.as_view(), name='blog_create'),
    path('comments/', views.CommentListView.as_view(), name='comment_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] 