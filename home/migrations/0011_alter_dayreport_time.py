# Generated by Django 4.1.1 on 2023-02-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_dayreport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dayreport", name="time", field=models.CharField(max_length=100),
        ),
    ]