from django.urls import path
from . import views
from .views import TaskDetailView, TaskDeleteView, TaskUpdateView


urlpatterns = [
    path('', views.home, name='task_list'),
    path('task/update/<str:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task/detail/<str:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/delete/<str:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]
