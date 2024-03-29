# Generated by Django 4.1.1 on 2023-01-21 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_newcostomer_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="DayReport",
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
                ("time", models.TimeField()),
                ("agenda_first_visit", models.CharField(max_length=100)),
                ("agenda_for_order", models.CharField(max_length=100)),
                ("agenda_for_trial", models.CharField(max_length=100)),
                ("next_plan", models.CharField(max_length=800)),
                (
                    "costomer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.newcostomer",
                    ),
                ),
            ],
        ),
    ]
