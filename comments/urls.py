from django.urls import path
from comments.views import CommentCreate, CommentDelete, CommentUpdate

app_name = 'comments'

urlpatterns = [
    path('comments_create/<int:pk>/', CommentCreate.as_view(), name="create"),
    path('comments_delete/<int:pk>/', CommentDelete.as_view(), name="delete"),
    path('comments_update/<int:pk>/', CommentUpdate.as_view(), name="update"),
]
