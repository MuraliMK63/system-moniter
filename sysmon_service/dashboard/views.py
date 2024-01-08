from django.shortcuts import render, redirect


from threading import Thread
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import LoginForm
from .models import UserAccount, TimeUsage
from .tracker import main_tracker
from .helper_func import apps_and_times

# Create your views here.

def loginview(request):
    forms = LoginForm()
    message = ''
    if request.method == "POST":
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = UserAccount.objects.filter(username = username, password = password).first()
            if user:
                tracker_thread = Thread(target = main_tracker, args = (user,))
                tracker_thread.start()
                return redirect(dashboardview, username)
            else:
                message = "Invalid User"
    return render(request, 'dashboard/login.html', context = {"form" : forms, "message" : message})

def dashboardview(request, username):
    data = TimeUsage.objects.filter(useraccount__username = username, date = datetime.now().date()).first().usage_json
    datas = apps_and_times(data)
    data = {"labels" : datas[0],"chartdata":datas[1],"chartLabel":"dashboard"}
    return render(request, 'dashboard/dashboard.html', context = {"data": datas})

class Data(APIView):
    def get(self,request):
        data = TimeUsage.objects.filter(useraccount__username = 'naresh', date = datetime.now().date()).first().usage_json
        datas = apps_and_times(data)
        data = {"labels" : datas[0],"chartdata":datas[1],"chartLabel":"dashboard"}
        return Response(data)