from django.urls import path
from todos.views import (
    TodoList,
    TodoView,
    TodoCreate,
    TodoUpdate,
    TodoDelete,
    TodoCompleteView,
)


urlpatterns = [
    path("", TodoList, name="todo_list"),
    path("todos/<int:id>", TodoView, name="todo_view"),
    path("create/", TodoCreate, name="todo_create"),
    path("update/<int:id>", TodoUpdate, name="todo_update"),
    path("delete/<int:id>", TodoDelete, name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]
