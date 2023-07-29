from django.urls import path
from topics.views import TopicsList, TopicCreate, TopicDetail, TopicUpdate, TopicDelete

app_name = 'topics'

urlpatterns = [
    path('', TopicsList.as_view(), name="home"),
    path('topic_create/', TopicCreate.as_view(), name="create"),
    path('topic_update/<int:pk>/', TopicUpdate.as_view(), name="update"),
    path('topic_delete/<int:pk>/', TopicDelete.as_view(), name="delete"),
    path('topic_detail/<int:pk>/', TopicDetail.as_view(), name="detail"),
]
