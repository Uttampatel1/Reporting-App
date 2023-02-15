from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class Report(models.Model):
    report_name = models.CharField(max_length=100)
    report_description = models.CharField(max_length=100)
    report_file = models.FileField(upload_to='reports/')

    def __str__(self):
        return self.report_name + ' - ' + self.report_description

class NewCostomer(models.Model):
    time = models.TimeField()
    date = models.DateField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    area = models.CharField(max_length=500)
    contactP = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    M_p = models.CharField(max_length=100)
    M_m = models.CharField(max_length=100)
    M_k = models.CharField(max_length=100)
    M_s = models.CharField(max_length=100)
    M_n = models.CharField(max_length=100)
    M_h = models.CharField(max_length=100)
    P_auto = models.CharField(max_length=100)
    P_sub = models.CharField(max_length=100)
    P_die = models.CharField(max_length=100)
    P_feb = models.CharField(max_length=100)
    P_are = models.CharField(max_length=100)
    P_def = models.CharField(max_length=100)
    P_pha = models.CharField(max_length=100)
    P_oth = models.CharField(max_length=100)
    E_code = models.CharField(max_length=100)
    E_use = models.CharField(max_length=100)
    E_price = models.CharField(max_length=100)
    N_cnc = models.CharField(max_length=100)
    N_vmc = models.CharField(max_length=100)
    N_vtl = models.CharField(max_length=100)
    N_bor = models.CharField(max_length=100)
    N_plano = models.CharField(max_length=100)
    monthly_po = models.CharField(max_length=100)
    E_close_m = models.CharField(max_length=100)
    remark = models.BooleanField(null=True)
   
    
    def __str__(self):
        # this function will return the name of the contact in the admin panel
        titale = self.name + " - " + self.email
        return titale

class DayReport(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    agenda_first_visit = models.BooleanField(null=True , default=False)
    agenda_for_order = models.BooleanField()
    agenda_for_trial = models.CharField(max_length=500)
    next_plan = models.CharField(max_length=800)

    def __str__(self):
        return self.name + " - " + self.time

class WeekReport(models.Model):
    name = models.CharField(max_length=200)
    area = models.CharField(max_length=1000)
    trial_item = models.CharField(max_length=600)
    materiel = models.CharField(max_length=600)
    other = models.CharField(max_length=900)

    def __str__(self):
        return self.name + " - " + self.area