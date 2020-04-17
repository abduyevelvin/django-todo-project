from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('todos/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('todos/<int:todo_pk>/', views.viewtodo, name='viewtodo'),
    path('todos/<int:todo_pk>/complete/', views.completetodo, name='completetodo'),
    path('todos/<int:todo_pk>/delete/', views.deletetodo, name='deletetodo'),
    path('todos/<int:todo_pk>/deleteconfirm/', views.deleteconfirm, name='deleteconfirm'),
]
