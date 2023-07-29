from django.urls import path
from topics.views import TopicsList

app_name = 'topics'

urlpatterns = [
    path('', TopicsList.as_view(), name="home")
]

