from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse



class TodoListView(LoginRequiredMixin, ListView):
    """
    Display a list of tasks for the authenticated user.
    Ordered by newest first.
    """
    model = TodoModel
    context_object_name = "Tasks"
    ordering = "-id"
    template_name = "todo_app/list_task.html"

    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user).order_by("-id")

class TodoCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new task for the logged-in user.
    """
    model = TodoModel
    fields = ["title"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        # Automatically assign the logged-in user to the task
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing task (title and completion status).
    """
    model = TodoModel
    context_object_name = "Tasks"
    fields = ["title", "status"]
    template_name = "todo_app/update_task.html"
    success_url = reverse_lazy("task_list")


class TodoCompleteView(LoginRequiredMixin, View):
    """
    Mark a task as completed.
    """
    model = TodoModel
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        # Get task by primary key
        task = TodoModel.objects.get(id=kwargs.get("pk"))

        # Mark as completed
        task.status = True
        task.save()

        return redirect(self.success_url)


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a task after confirmation.
    Only allows deletion of tasks belonging to the current user.
    """
    model = TodoModel
    context_object_name = "Task"
    template_name = "todo_app/delete.html"
    success_url = reverse_lazy("task_list")

    def get_queryset(self):
        # Restrict deletion to tasks owned by the logged-in user
        return self.model.objects.filter(user=self.request.user)