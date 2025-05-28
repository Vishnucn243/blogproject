from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.BlogListView.as_view(),name='blog_list'),
    path('blog/<int:pk>/',views.BlogDetailView.as_view(),name='blog_detail'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
] 