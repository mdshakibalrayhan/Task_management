# Generated by Django 5.0.6 on 2024-10-04 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='task_category_relation',
        ),
    ]
