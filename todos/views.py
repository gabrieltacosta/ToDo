from django.shortcuts import get_object_or_404, redirect, render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from .models import Todo
from .forms import TodoForm, TodoFormDelete


# Create your views here.
def TodoList(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})


def TodoView(request, id):
    todo = get_object_or_404(Todo, pk=id)
    return render(request, "todos/todo.html", {"todo": todo})


def TodoCreate(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")
    else:
        form = TodoForm()
        return render(request, "todos/todo_form.html", {"form": form})


def TodoUpdate(request, id):
    todo = get_object_or_404(Todo, pk=id)
    form = TodoForm(instance=todo)

    if (request.method == "POST"):
        form = TodoForm(request.POST, instance=todo)

        if (form.is_valid()):
            todo.save()
            return redirect("todo_list")
        else:
            return render(request, "todos/todo_update.html", {"form": form, "todo": todo})
    else:
        return render(request, "todos/todo_update.html", {"form": form, "todo": todo})


def TodoDeleteConfirm(request, id):
    todo = get_object_or_404(Todo, pk=id)
    form = TodoFormDelete(instance=todo)
    return render(request, "todos/Todo_confirm_delete.html", {"form": form, "todo": todo})


def TodoDelete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    return redirect("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")
