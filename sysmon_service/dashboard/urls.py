from rest_framework.urls import path
from .views import loginview, dashboardview, Data

# Create your urls here

urlpatterns = [
    path('login/', loginview, name = 'login_view'),
    path('dashboard/<str:username>/', dashboardview, name = 'dashboard_view'),
    path('data/',Data.as_view())
]
