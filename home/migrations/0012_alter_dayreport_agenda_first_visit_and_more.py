# Generated by Django 4.1.1 on 2023-02-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_alter_dayreport_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dayreport",
            name="agenda_first_visit",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="newcostomer",
            name="remark",
            field=models.BooleanField(default=False),
        ),
    ]
