# Generated by Django 4.2 on 2023-04-08 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_todo_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='grade',
        ),
    ]