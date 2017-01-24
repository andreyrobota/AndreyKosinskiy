from django.conf.urls import url
from idea.views import addIdea

urlpatterns = [
    url(r'^', addIdea, name='addIdea'),
]