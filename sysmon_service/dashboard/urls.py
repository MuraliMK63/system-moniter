from rest_framework.urls import path
from .views import  dashboardview, data, DayDataView, WeekDataView

# Create your urls here

urlpatterns = [
    path('dashboard/<str:username>/', dashboardview, name = 'dashboard_view'),
    path('data/', data, name ='unknown_data_view'),
    path('fulldata/', DayDataView.as_view(), name = 'full_data_view'),
    path('weekData/', WeekDataView.as_view(), name = 'week_data_view')
]
