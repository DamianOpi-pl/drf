# Generated by Django 5.0.2 on 2024-02-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_remove_bookssearch_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("authors", models.TextField()),
                ("published_date", models.CharField(max_length=10)),
                ("categories", models.TextField()),
                ("average_rating", models.IntegerField()),
                ("ratings_count", models.IntegerField()),
                ("thumbnail", models.CharField(max_length=200)),
            ],
        ),
    ]
