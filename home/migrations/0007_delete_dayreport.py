# Generated by Django 4.1.1 on 2023-02-13 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_alter_dayreport_agenda_first_visit_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="DayReport",),
    ]