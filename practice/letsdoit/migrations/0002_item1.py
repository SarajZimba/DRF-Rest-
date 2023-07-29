# Generated by Django 4.1.7 on 2023-07-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("letsdoit", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item1",
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
                ("name", models.CharField(max_length=200)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]