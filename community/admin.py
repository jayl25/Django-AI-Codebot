from django.contrib import admin
from .models import UserPost, Comment

# Register your models here.

admin.site.register(UserPost)
admin.site.register(Comment)