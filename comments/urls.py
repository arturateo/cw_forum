from django.urls import path
from comments.views import CommentCreate

app_name = 'comments'

urlpatterns = [
    path('comments_create/<int:pk>/', CommentCreate.as_view(), name="create"),
]
