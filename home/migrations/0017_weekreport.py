# Generated by Django 4.1.1 on 2023-02-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_alter_dayreport_agenda_first_visit"),
    ]

    operations = [
        migrations.CreateModel(
            name="WeekReport",
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
                ("area", models.CharField(max_length=1000)),
                ("trial_item", models.CharField(max_length=600)),
                ("materiel", models.CharField(max_length=600)),
                ("other", models.CharField(max_length=900)),
            ],
        ),
    ]
