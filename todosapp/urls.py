from django.urls import path
from .views import TodosListView, TodosDetailView, TodosCreateView, TodosDeleteView, TodosUpdateView

urlpatterns = [
    path('todos/', TodosListView.as_view()),
    path('todos/create', TodosCreateView.as_view()),
    path('todos/<int:pk>/', TodosDetailView.as_view()),
    path('todos/update/<int:pk>/', TodosUpdateView.as_view()),
    path('todos/delete/<int:pk>/', TodosDeleteView.as_view()),
]
