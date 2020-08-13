from django import forms

from ToDoDashboard.models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    class Meta:
        fields = ['description', 'label', 'comment', 'dashboard_column', 'start_date', 'due_date',
                  'time_estimate_hours']
        model = ToDoItem

    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('due_date')
        estimated_hours = self.cleaned_data.get('time_estimate_hours')

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError('Dates are incorrect:'
                                            'due_date goes behind start_date')

        from datetime import timedelta
        if start_date + timedelta(hours=estimated_hours) > end_date:
            raise forms.ValidationError('Inconsistent dates and estimation. '
                                        'start_date+estimated_hours goes after '
                                        'due_date')

        return self.cleaned_data
