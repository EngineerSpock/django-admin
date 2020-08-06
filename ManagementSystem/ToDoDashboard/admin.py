from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from django.utils.safestring import mark_safe

from ToDoDashboard.models import Member, Dashboard, DashboardColumn, ToDoItem
from users.models import User


class MyAdminSite(admin.AdminSite):

    def get_urls(self):
        urlpatterns = super().get_urls()
        urlpatterns += [
            # add later
        ]
        return urlpatterns


admin.site = MyAdminSite()


class ColumnInline(admin.StackedInline):
    model = DashboardColumn


# @admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    inlines = [ColumnInline, ]

    fields = (('title', 'is_public'), 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    list_display = ('id', 'title', 'get_owner', 'created_at', 'updated_at', 'is_public')
    list_display_links = ('id', 'title')
    list_editable = ('is_public',)

    # def get_list_display(self, record):
    #     ld = ['id', 'title', 'get_owner', 'is_public']
    #
    #     if record.user.is_superuser:
    #         ld += ['created_at', 'updated_at']
    #     return ld

    def get_owner(self, rec):
        return rec.owner.user.username

    get_owner.short_description = 'Owner'


class ToDoItemInline(admin.TabularInline):
    model = ToDoItem

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 1
        else:
            return 5

    show_change_link = True
    fk_name = 'dashboard_column'
    # verbose_name = 'ToDo Item'
    # verbose_name_plural = 'ToDo Items'


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('title', 'dashboard', 'created_at', 'updated_at')
    fields = ('title', 'dashboard', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    inlines = [ToDoItemInline]


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'created_at', 'updated_at', 'get_avatar',)

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="75">')
        else:
            return '-'

    get_avatar.short_description = 'THUMBNAIL'
    empty_value_display = 'UNSET'


class ToDoItemFilter(admin.SimpleListFilter):
    title = 'Difficulty'
    parameter_name = 'time_estimate_hours'

    def lookups(self, request, model_admin):
        return (
            ('easy', 'Easy'),
            ('average', 'Average'),
            ('hard', 'Hard'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'easy':
            return queryset.filter(time_estimate_hours__lt=2)
        elif self.value() == 'average':
            return queryset.filter(time_estimate_hours__gte=2,
                                   time_estimate_hours__lte=8)
        elif self.value() == 'hard':
            return queryset.filter(time_estimate_hours__gt=8)


class ToDoItemAdmin(admin.ModelAdmin):

    def add_one_hour_to_estimated_time(self, request, queryset):
        for rec in queryset:
            rec.time_estimate_hours += 1
            rec.save()
        self.message_user(request, 'Done')

    add_one_hour_to_estimated_time.short_description = 'Add 1 Hour'

    actions = ('add_one_hour_to_estimated_time',)

    # fields = ('description', 'comment', 'label',
    #           ('due_date', 'time_estimate_hours'))
    save_on_top = True

    fieldsets = (
        ('Main', {
            'fields': ('description', 'comment', ('label', 'dashboard_column'))
        }),
        ('Estimations', {
            'fields': (('start_date', 'due_date'), 'time_estimate_hours'),
            'description': 'Dates and Times',
            'classes': ('collapse',)
        }),
    )

    list_display = ('description', 'label', 'comment', 'due_date',
                    'time_estimate_hours',)
    list_editable = ('label', 'time_estimate_hours')

    search_fields = ('description', 'comment')
    list_filter = ('label', ToDoItemFilter,)

    sortable_by = ('label', 'due_date', 'time_estimate_hours',)
    ordering = ('due_date', 'time_estimate_hours')

    actions_on_bottom = True

from django.contrib.auth.admin import UserAdmin, GroupAdmin
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)

admin.site.register(Member, MemberAdmin)
admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(DashboardColumn, ColumnAdmin)
admin.site.register(ToDoItem, ToDoItemAdmin)

admin.site.site_header = 'ADMIN PANEL'
admin.site.site_title = 'SITE ADMIN'
admin.site.index_title = 'ADMINISTRATION'
