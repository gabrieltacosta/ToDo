from django.contrib import admin
from django.urls import path
from todos.views import TodolListView, TodoCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodolListView.as_view(), name='todo_list'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
]
