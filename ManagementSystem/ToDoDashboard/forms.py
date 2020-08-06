from django import forms

from ToDoDashboard.models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    class Meta:
        fields = ['description', 'label', 'comment', 'dashboard_column', 'start_date', 'due_date',
                  'time_estimate_hours']
        model = ToDoItem
