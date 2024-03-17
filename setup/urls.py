from django.contrib import admin
from django.urls import path
from todos.views import TodolListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodolListView.as_view(), name='todo_list'),
]
