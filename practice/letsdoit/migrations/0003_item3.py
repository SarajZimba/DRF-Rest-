# Generated by Django 4.1.7 on 2023-07-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("letsdoit", "0002_item1"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item3",
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
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
