from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='task_list'),
    path('create/', views.TodoCreateView.as_view(), name='create_task'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='update_task'),
    path("complete/<int:pk>/", views.TodoCompleteView.as_view(), name="complete_task"),
    path("delete/<int:pk>/", views.TodoDeleteView.as_view(), name="delete_task"),

]
