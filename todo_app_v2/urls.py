from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo_list'),
    path('create/', views.CreateTodoView.as_view(), name='create_todo'),
    path('<int:pk>/delete/', views.DeleteTodoView.as_view(), name='delete_todo'),
    path('<int:pk>/edit/', views.UpdateTodoView.as_view(), name='update_todo')
]