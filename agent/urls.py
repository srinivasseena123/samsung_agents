from django.urls import path
from . import views

urlpatterns = [
    path('', views.AgentList.as_view(), name='agent-list'),
    
]
