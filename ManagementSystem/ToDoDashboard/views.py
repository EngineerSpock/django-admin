from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, UpdateView

from ToDoDashboard.forms import ToDoItemForm
from ToDoDashboard.models import Dashboard, ToDoItem


def index(request):
    print(request)
    return HttpResponse('<h1>Hello World!</h1>')


class DashboardListView(ListView):
    model = Dashboard
    template_name = 'kanban.html'
    ordering = 'title'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Kanban'
        context['has_permission'] = True
        return context


class DashboardDetailView(DetailView, admin.ModelAdmin):
    model = Dashboard
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.title
        context['has_permission'] = True
        context['task_form'] = ToDoItemForm()
        return context


class AjaxableResponseMixin:

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = serializers.serialize('json', [self.object])
            return JsonResponse(data, safe=False)
        else:
            return response


class TodoItemUpdate(AjaxableResponseMixin, UpdateView):
    model = ToDoItem
    fields = ['dashboard_column']
    success_url = '/'
