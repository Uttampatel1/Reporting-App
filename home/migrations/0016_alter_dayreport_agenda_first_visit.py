# Generated by Django 4.1.1 on 2023-02-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_alter_dayreport_agenda_first_visit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dayreport",
            name="agenda_first_visit",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
