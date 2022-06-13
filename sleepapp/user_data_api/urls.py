from django.urls import path
from . import views

urlpatterns = [
    path('api/sleepData', views.sleepDataList.as_view(), name='sleepData_list'), 
    path('api/sleepData/<int:pk>', views.sleepDataDetail.as_view(), name='sleepData_detail'),
]
