from django.shortcuts import render
from fund.models import Fundmodel
from django.http import JsonResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def calenderPage(request):
   allfund = Fundmodel.objects.all()
   context = {
       "fund":allfund,
   }
   return render(request,'cal.html',context)

def allfund(request):
    fund = Fundmodel.objects.filter(milik_id=request.user.id).all()
    out=[]
    for uang in fund:
        out.append({
            'title':"Rp."+str(uang.Jumlah)+",-",
            'start':uang.Tanggal.strftime("%m/%d/%Y"),
            'end':uang.Tanggal.strftime("%m/%d/%Y"),
        })
    return JsonResponse(out,safe=False)
# Create your views here.
