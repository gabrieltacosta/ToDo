from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ("title", "description", "deadline", "finished_at")


class TodoFormDelete(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ("title",)
