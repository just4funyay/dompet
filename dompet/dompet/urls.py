"""
URL configuration for dompet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from reglog import views
from fund import views as fundviews 
from home import views as homeviews
from calender import views as calenderviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',homeviews.Homepage,name='home'),
    path('logout/',views.logout,name='logout'),
    path('fund/',fundviews.fundpage,name='fund'),
    path('delete/<int:fund_id>',homeviews.Deletedata,name="delete"),
    path('fund/<int:fund_id>',homeviews.EditData,name="edit"),
    path('calender/',calenderviews.calenderPage,name='calender'),
    path('allfund/',calenderviews.allfund,name='calenderisi'),
    path('chart/',fundviews.stats,name="chartcalender"),
    path('Viewfund/<int:fund_id>',homeviews.Viewfund,name="view"),
    
]
urlpatterns += staticfiles_urlpatterns()