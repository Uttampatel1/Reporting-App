from django.contrib import admin
from .models import Report, NewCostomer , DayReport ,WeekReport

# Register your models here.

admin.site.register(Report)
admin.site.register(NewCostomer)
admin.site.register(DayReport)
admin.site.register(WeekReport)