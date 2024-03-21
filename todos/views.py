from django.shortcuts import get_object_or_404, redirect, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, View
from .models import Todo


# Create your views here.
def TodoList(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})

def TodoView(request, id):
    todo = get_object_or_404(Todo, pk=id)
    return render(request, "todos/todo.html", {"todo": todo})

#class TodolListView(ListView):
#    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline", "finished_at"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")
