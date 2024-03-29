# Generated by Django 4.1.1 on 2023-01-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewCostomer",
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
                ("date", models.DateField()),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=500)),
                ("area", models.CharField(max_length=500)),
                ("contactP", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("M_p", models.CharField(max_length=100)),
                ("M_m", models.CharField(max_length=100)),
                ("M_k", models.CharField(max_length=100)),
                ("M_s", models.CharField(max_length=100)),
                ("M_n", models.CharField(max_length=100)),
                ("M_h", models.CharField(max_length=100)),
                ("P_auto", models.CharField(max_length=100)),
                ("P_sub", models.CharField(max_length=100)),
                ("P_die", models.CharField(max_length=100)),
                ("P_feb", models.CharField(max_length=100)),
                ("P_are", models.CharField(max_length=100)),
                ("P_def", models.CharField(max_length=100)),
                ("P_pha", models.CharField(max_length=100)),
                ("P_oth", models.CharField(max_length=100)),
                ("E_code", models.CharField(max_length=100)),
                ("E_use", models.CharField(max_length=100)),
                ("E_price", models.CharField(max_length=100)),
                ("N_cnc", models.CharField(max_length=100)),
                ("N_vmc", models.CharField(max_length=100)),
                ("N_vtl", models.CharField(max_length=100)),
                ("N_bor", models.CharField(max_length=100)),
                ("N_plano", models.CharField(max_length=100)),
                ("monthly_po", models.CharField(max_length=100)),
                ("E_close_m", models.CharField(max_length=100)),
                ("remark", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Report",
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
                ("report_name", models.CharField(max_length=100)),
                ("report_description", models.CharField(max_length=100)),
                ("report_file", models.FileField(upload_to="reports/")),
            ],
        ),
    ]
