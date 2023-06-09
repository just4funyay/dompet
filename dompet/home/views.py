from django.shortcuts import render,redirect
from fund.models import Fundmodel
from django.db.models import Sum
from fund.views import fundpage
from datetime import datetime
from django.contrib.auth.decorators import login_required
import calendar
@login_required(login_url='/login')
def Homepage(request):

     jumlahnya = Fundmodel.objects.filter(milik_id=request.user.id).aggregate(Sum('Jumlah',default=0))
     data_list = Fundmodel.objects.filter(milik_id=request.user.id).all()
     bulannn = Fundmodel.objects.filter(milik_id=request.user.id).order_by('-Tanggal').values('id','kategori','Jumlah','Tanggal__day','Tanggal__month','Tanggal__year','Deskripsi')
     for x in bulannn:
          x["Tanggal__month"]=calendar.month_abbr[int(x["Tanggal__month"])]
     context = {'jumlahnya':jumlahnya,
                'data':data_list,
                'bulannn':bulannn,
                }
     return render(request,'index.html',context)

def Deletedata(request, fund_id):
     hapus = Fundmodel.objects.get(id=fund_id)
     hapus.delete()
     return redirect('home')
def EditData(request, fund_id):
     link = Fundmodel.objects.get(id=fund_id)
     fund = Fundmodel.objects.filter(id=fund_id).all()
     total = Fundmodel.objects.filter(milik_id=request.user.id).aggregate(Sum('Jumlah',default=0))
     for x in fund:
          if x.kategori == "Pengeluaran":
               x.Jumlah=(-1)*(x.Jumlah)
     if request.method == "POST":
          kat = request.POST.get('kate')
          keluar=int(request.POST.get('duid'))
          if kat == 'Pengeluaran':     
              link.kategori = kat
              link.Tanggal = request.POST.get('tangal')
              link.Jumlah = (-1)*keluar
              link.Deskripsi = request.POST.get('desc')
              link.save()
              
          elif kat=='Pemasukan':
               link.kategori = kat
               link.Tanggal = request.POST.get('tangal')
               link.Jumlah = keluar
               link.Deskripsi = request.POST.get('desc')
               link.save()
          return redirect(Homepage)
     context={'link':link,'fund':fund,'fund_id':fund_id,'total':total}
     return render(request,'fundd.html',context)

def Viewfund(request, fund_id):
     total = Fundmodel.objects.filter(milik_id=request.user.id).aggregate(Sum('Jumlah',default=0))
     fund = Fundmodel.objects.filter(id=fund_id).all()
     for x in fund:
          if x.kategori == "Pengeluaran":
               x.Jumlah=(-1)*(x.Jumlah)

     context={'fund':fund,'fund_id':fund_id,'total':total}
     return render(request,'viewfund.html',context)