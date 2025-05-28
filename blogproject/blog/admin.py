from django.contrib import admin
from .models import Blog, Profile

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','author','created_at','updated_at')
    list_filter=('created_at','author')
    search_fields=('title','content')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','location','birth_date')
    search_fields=('user__username','location')
