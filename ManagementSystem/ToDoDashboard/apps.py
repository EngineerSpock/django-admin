from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class ToDoDashboardConfig(AppConfig):
    name = 'ToDoDashboard'
    verbose_name = 'ToDo Dashboard'


class MyAdminConfig(AdminConfig):
    default_site = 'ToDoDashboard.admin.MyAdminSite'
