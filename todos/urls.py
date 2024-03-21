from django.urls import path
from todos.views import (
    TodoList,
    TodoView,
#    TodoCreateView,
#    TodoUpdateView,
#    TodoDeleteView,
#    TodoCompleteView,
)


urlpatterns = [
    path("", TodoList, name="todo_list"),
    path("todos/<int:id>", TodoView, name="todo_view"),
#    path("create/", TodoCreateView.as_view(), name="todo_create"),
#    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
#    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
#    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]
