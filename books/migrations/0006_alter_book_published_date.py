# Generated by Django 5.0.2 on 2024-02-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0005_alter_book_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="published_date",
            field=models.CharField(max_length=10, null=True),
        ),
    ]