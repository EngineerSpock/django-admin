from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models, migrations

from ToDoDashboard.models import *


def load_data(apps, schema_editor):
    user = get_user_model()
    user1 = user.objects.create_user(username='alice',
                                     email='alice@company.com',
                                     password='super12')
    user1.save()

    member1 = Member(user=user1)
    member1.save()

    alice_dashboard = Dashboard(title='AliceDashboard', owner=member1)
    alice_dashboard.save()

    column = DashboardColumn(title='Prioritized', dashboard=alice_dashboard)
    column.save()

    item1 = ToDoItem(dashboard_column=column, description='Build metrics on sale stats', label='sales',
                     comment='need a script loading data', time_estimate_hours=16,
                     start_date='2020-10-29', due_date='2020-11-05'
                     )

    item2 = ToDoItem(dashboard_column=column, description='Reviews on YouTube', label='sales',
                     time_estimate_hours=24, comment='multiple videos with testimonials',
                     start_date='2020-10-29', due_date='2020-11-07')

    item3 = ToDoItem(dashboard_column=column, description='Gather some info about E-learning platforms',
                     label='marketing', comment='use different sources', time_estimate_hours=4,
                     start_date='2020-10-29', due_date='2020-11-05')

    item1.save()
    item2.save()
    item3.save()

    column_monday = DashboardColumn(title='Monday', dashboard=alice_dashboard)
    column_monday.save()

    column_tuesday = DashboardColumn(title='Tuesday', dashboard=alice_dashboard)
    column_tuesday.save()

    item_monday_1 = ToDoItem(dashboard_column=column_monday, description='Generate subtitles', comment='use .vtt',
                             label='low priority', time_estimate_hours=4, start_date='2020-11-02',
                             due_date='2020-11-05')

    item_monday_2 = ToDoItem(dashboard_column=column_monday, description='Learn new Python features',
                             comment='look at the official docs', label='work',
                             time_estimate_hours=3, start_date='2020-11-02', due_date='2020-11-02')

    item_monday_3 = ToDoItem(dashboard_column=column_monday, description='Call Boss',
                             comment='via WhatsApp', label='average priority',
                             time_estimate_hours=1, start_date='2020-11-02', due_date='2020-11-02')

    item_monday_4 = ToDoItem(dashboard_column=column_monday, description='Water the herbs',
                             comment='in office', label='average priority',
                             time_estimate_hours=1, start_date='2020-11-02', due_date='2020-11-02')

    item_tuesday_1 = ToDoItem(dashboard_column=column_tuesday, description='Write a blog article',
                              label='collaboration', comment='invite a co-author',
                              time_estimate_hours=2, start_date='2020-11-03', due_date='2020-11-03')

    item_tuesday_2 = ToDoItem(dashboard_column=column_tuesday, description='Extract separate videos',
                              label='average priority', comment='videos should be "self-valuable"',
                              time_estimate_hours=3, start_date='2020-11-03', due_date='2020-11-03')

    item_tuesday_3 = ToDoItem(dashboard_column=column_tuesday, description='Quiz for subscribers',
                              label='collaboration', comment='use presentation',
                              time_estimate_hours=1, start_date='2020-11-03', due_date='2020-11-03')

    item_tuesday_4 = ToDoItem(dashboard_column=column_tuesday, description='Help colleague with Presentation',
                              label='collaboration', comment='use supplementary materials',
                              time_estimate_hours=2, start_date='2020-11-03', due_date='2020-11-03')

    item_monday_1.save()
    item_monday_2.save()
    item_monday_3.save()
    item_monday_4.save()

    item_tuesday_1.save()
    item_tuesday_2.save()
    item_tuesday_3.save()
    item_tuesday_4.save()


class Migration(migrations.Migration):
    dependencies = [
        ('ToDoDashboard', '0002_auto_20200715_1229'),
    ]
    operations = [
        migrations.RunPython(load_data)
    ]