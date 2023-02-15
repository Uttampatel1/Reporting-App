from django.shortcuts import render ,redirect
from django.http import HttpResponse
from home.models import Report, NewCostomer , DayReport , WeekReport
import sqlite3
import pandas as pd
from django.contrib import messages
from datetime import datetime ,timedelta
from django.db.models import Q
import datetime
from .forms import DataForm
import io
from django.contrib.auth.models import User 
from django.contrib.auth import logout , authenticate , login
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")

def loginUser(request):
    if request.method == "POST":
        # check if user exists
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, "login.html")
    return render(request, "login.html")

def logoutUser(request):    
    logout(request)
    return redirect("/login")

def newcostmer(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        # city = request.POST.get("city")
        # state = request.POST.get("state")
        # zip_code = request.POST.get("zip_code")
        area = request.POST.get("area")
        contactP = request.POST.get("contactP")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        M_p = request.POST.get("m_p")
        M_m = request.POST.get("m_m")
        M_k = request.POST.get("m_k")
        M_s = request.POST.get("m_s")
        M_n = request.POST.get("m_n")
        M_h = request.POST.get("m_h")
        P_auto = request.POST.get("p_auto")
        P_sub = request.POST.get("p_sub")
        P_die = request.POST.get("p_die")
        P_feb = request.POST.get("p_feb")
        P_are = request.POST.get("p_are")
        P_def = request.POST.get("p_def")
        P_pha = request.POST.get("p_pha")
        P_oth = request.POST.get("p_oth")
        E_code = request.POST.get("e_code")
        E_use = request.POST.get("e_use")
        E_price = request.POST.get("e_price")
        N_cnc = request.POST.get("n_cnc")
        N_vmc = request.POST.get("n_vmc")
        N_vtl = request.POST.get("n_vtl")
        N_bor = request.POST.get("n_bor")
        N_plano = request.POST.get("n_plano")
        monthly_po = request.POST.get("monthly_po")
        E_close_m = request.POST.get("e_close_m")
        remark = request.POST.get("remark")
        print(name,address,area,contactP,phone,email,M_p,M_m,M_k,M_s,M_n,M_h,P_auto,P_sub,P_die,P_feb,P_are,P_def,P_pha,P_oth,E_code,E_use,E_price,N_cnc,N_vmc,N_vtl,N_bor,N_plano,monthly_po,E_close_m,remark)
        newcostomer = NewCostomer(time=datetime.datetime.now(),date=datetime.datetime.now(),name=name,address=address,area=area,contactP=contactP,phone=phone,email=email,M_p=M_p,M_m=M_m,M_k=M_k,M_s=M_s,M_n=M_n,M_h=M_h,P_auto=P_auto,P_sub=P_sub,P_die=P_die,P_feb=P_feb,P_are=P_are,P_def=P_def,P_pha=P_pha,P_oth=P_oth,E_code=E_code,E_use=E_use,E_price=E_price,N_cnc=N_cnc,N_vmc=N_vmc,N_vtl=N_vtl,N_bor=N_bor,N_plano=N_plano,monthly_po=monthly_po,E_close_m=E_close_m,remark=remark)
        newcostomer.save()
        messages.success(request, "Your Data has been sent!")
      
    return render(request,"newcostmer.html")

def weekplan(request):
    if request.user.is_anonymous:
        return redirect("/login")
    names = NewCostomer.objects.values_list('name', flat=True)
    area = NewCostomer.objects.values_list('area', flat=True)
  
    if request.method == "POST":
        name = request.POST.get("name")
        area = request.POST.get("area")
        trial_item = request.POST.get("trial_item")
        materiel = request.POST.get("materiel")
        other = request.POST.get("other")
        print(name,area,trial_item,materiel,other)
        data = WeekReport(name=name,area=area,trial_item=trial_item,materiel=materiel,other=other)
        data.save()
        messages.success(request, "Your Data has been sent!")
       
    return render(request, 'weekReport.html', {'names': names,'areas': area})


def new_customers_on_date(request, date):
    new_customers_on_specific_date = NewCostomer.objects.filter(date__contains=date)
    names = new_customers_on_specific_date.values_list('name', flat=True)
    print(new_customers_on_specific_date)
    return render(request, 'weekReport.html', {'names': names,'new_customers': new_customers_on_specific_date, 'date': date})

def dayplan(request):
    if request.user.is_anonymous:
        return redirect("/login")
    names = NewCostomer.objects.values_list('name', flat=True)
    if request.method == "POST":
        name = request.POST.get("name1")
        time = request.POST.get("time")
        first_visit = request.POST.get("first_visit")
        for_order_r = request.POST.get("flexRadioDefault")
        for_trial = request.POST.get("flexRadioDefault1")
        next_plan = request.POST.get("next_plan")
        print(name,time,first_visit,for_order_r,for_trial,next_plan)
        dayplan = DayReport(name=name,time=time,agenda_first_visit=first_visit,agenda_for_order=for_order_r,agenda_for_trial=for_trial,next_plan=next_plan)
        dayplan.save()
        messages.success(request, "Your Data has been sent!")   
    return render(request, 'DailyReport.html', {'names': names})


def last_7_days_data(request):
    today = datetime.date.today()
    last_week = today - timedelta(days=7)
    last_7_days_data = NewCostomer.objects.filter(date__range=(last_week, today))

    return render(request, 'last_7_days_data.html', {'data': last_7_days_data})

def retrieve_data(request):
    if request.method == 'GET':
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        form = DataForm(request.GET)
        data = NewCostomer.objects.filter(date__range=(start_date, end_date))
        print(data)
        return render(request, 'data.html', {'data': data})
        # return render(request, 'weekReport.html', {'names': data.name,'areas': data.area})
    # if request.method == 'POST':
    #     form = DataForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         start_date = form.cleaned_data['start_date']
    #         end_date = form.cleaned_data['end_date']
    #         data = NewCostomer.objects.filter(name=name, date__range=(start_date, end_date))
    #         return render(request, 'data.html', {'data': data})
    # else:
    #     form = DataForm()
    # return render(request, 'retrieve_data.html', {'form': form})


def dowonload_newco(request):
    # Query data from the Django SQLite3 database
    data = NewCostomer.objects.all()

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(list(data.values()))

    # Export data to Excel file in memory
    excel_file = io.BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    # Create an HTTP response with the Excel file as an attachment
    response = HttpResponse(excel_file.read(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=CostomerData.xlsx'
    return response

def dowonload_dayreport(request):
    # Query data from the Django SQLite3 database
    data = DayReport.objects.all()
    
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(list(data.values()))

    # Export data to Excel file in memory
    excel_file = io.BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    # Create an HTTP response with the Excel file as an attachment
    response = HttpResponse(excel_file.read(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=daydata.xlsx'
    return response

def dowonload_weekRepo(request):
    # Query data from the Django SQLite3 database
    data = WeekReport.objects.all()

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(list(data.values()))

    # Export data to Excel file in memory
    excel_file = io.BytesIO()
    df.to_excel(excel_file, index=False)
    excel_file.seek(0)

    # Create an HTTP response with the Excel file as an attachment
    response = HttpResponse(excel_file.read(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=weekdata.xlsx'
    return response
