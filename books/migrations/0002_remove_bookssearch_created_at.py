# Generated by Django 5.0.2 on 2024-02-14 11:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookssearch",
            name="created_at",
        ),
    ]
