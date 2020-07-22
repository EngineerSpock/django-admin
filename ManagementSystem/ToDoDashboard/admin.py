from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from ToDoDashboard.models import Member, Dashboard, DashboardColumn, ToDoItem
from users.models import User

admin.site.register(User, UserAdmin)

admin.site.register(Member)
admin.site.register(Dashboard)
admin.site.register(DashboardColumn)
admin.site.register(ToDoItem)