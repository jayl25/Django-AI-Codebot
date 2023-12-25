

from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name="posts"),
    path('edit_post/<int:post_id>', views.edit_post, name="edit_post"),
    path('reply/<int:post_id>', views.posts, name="reply"),
    path('delete/<int:post_id>', views.delete_post, name="delete_post"),
]