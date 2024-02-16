from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


from threading import Thread
from datetime import datetime, timedelta
import time
import os

from .forms import LoginForm
from .models import UserAccount, TimeUsage
from .tracker import main_tracker
from .helper_func import apps_and_times, apps_and_duration, days_and_times

def dashboardview(request, username):
    data = TimeUsage.objects.filter(useraccount__username = username, date = datetime.now().date())
    if not data:
        return Response('No data found.')
    data = data.first().usage_json
    datas = apps_and_times(data)
    return render(request, 'dashboard/dashboard.html', context = {"data": datas})

@api_view(('GET', ))
def data(request):
    username = os.getlogin()
    data = TimeUsage.objects.filter(useraccount__username = username, date = datetime.now().date())
    if not data:
        return Response('No data found.')
    data = data.first().usage_json
    datas = apps_and_times(data)
    data = {"labels" : datas[0],"chartdata":datas[1],"chartLabel":"dashboard"}
    return Response(data)

## API's for React Project

class DayDataView(APIView):
    def get(self, request):
        username = os.getlogin()
        data = TimeUsage.objects.filter(useraccount__username = username, date = datetime.now().date())
        if not data:
            return Response('No data found.')
        data = data.first().usage_json 
        final_data, appnames, timings = apps_and_duration(data)
        return Response([final_data, [appnames, timings]])
    
class WeekDataView(APIView):
    def get(self, request):
        username = os.getlogin()
        day = datetime.now().weekday()
        start_week_date = datetime.now().date() - timedelta(days = day)
        data = TimeUsage.objects.filter(useraccount__username = username, date__gte = start_week_date).values()
        final_data = days_and_times(data)
        return Response(final_data)
