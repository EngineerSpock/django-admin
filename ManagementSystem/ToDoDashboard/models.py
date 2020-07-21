from django.db import models

from ManagementSystem.settings import AUTH_USER_MODEL


class Member(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    avatar = models.ImageField(upload_to='photos/', blank=True)

    department = models.TextField(null=True, blank=True)


class Dashboard(models.Model):
    title = models.CharField(max_length=128)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='member')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='LAST UPDATE')

    is_public = models.BooleanField(default=True)


class DashboardColumn(models.Model):
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ToDoItem(models.Model):
    dashboard_column = models.ForeignKey(DashboardColumn, on_delete=models.CASCADE)

    description = models.TextField()
    label = models.CharField(max_length=128, blank=True)

    start_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    time_estimate_hours = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    subtask_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
