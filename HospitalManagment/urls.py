"""HospitalManagment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hospital_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.index, name='home'),
    path('home/appointments/', views.patient_1, name='appointment'),
    path('home/appointments/add', views.add_appointment, name='add'),
    path('home/doctors/',views.doctor, name='to_doctor'),
    path('home/doctors/add', views.add_doctor, name='add_doctor'),
    path('home/appointments/edit/<int:p_id>', views.edit_appointment, name='edit'),
    path('home/appointments/delete/<int:p_id>', views.del_appointment),
    path('home/doctors/edit/<d_id>', views.update_doctor),
    path('home/doctors/del/<d_id>', views.del_doc),
    path('register/', views.register, name='register'),
    path('', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout')
]
