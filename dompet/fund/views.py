from django.shortcuts import render,redirect
from .forms import fundForm
from .models import Fundmodel
from reglog import views as reglogviews
from home import views as homeviews
import datetime
from django.views import View
from django.db.models import Sum
import calendar
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')    
def fundpage(request):
    jumlahnya = Fundmodel.objects.filter(milik_id=request.user.id).aggregate(Sum('Jumlah',default=0))
    if request.method == 'POST':
        
                kat = request.POST.get('kate')
                keluar=int(request.POST.get('duid'))
                if kat == 'Pengeluaran':     
                    masuk = Fundmodel.objects.create(
                     kategori=kat,
                     Tanggal=request.POST.get('tangal'),
                     Jumlah=(-1)*keluar,
                     Deskripsi=request.POST.get('desc'),
                     Catatan=request.POST.get('catatan'),
                     milik_id=request.user.id)
                    masuk.save()
                elif kat=='Pemasukan':
                     masuk = Fundmodel.objects.create(
                     kategori=kat,
                     Tanggal=request.POST.get('tangal'),
                     Jumlah=request.POST.get('duid'),
                     Deskripsi=request.POST.get('desc'),
                     Catatan=request.POST.get('catatan'),
                     milik_id=request.user.id)
                     masuk.save()
                return redirect(homeviews.Homepage)
    else:
        fundform = fundForm()
    return render(request,'fundd.html',{'jumlahnya':jumlahnya})

def Editform(request, fund_id):
     fund = Fundmodel.objects.get(pk=fund_id)
     return render(request,'fund/<int:>')

@login_required(login_url='/login') 
def stats(request):
     labels=[]
     data1 = []
     data2 = []
     pengeluaran=0
     pemasukan=0
     month=datetime.datetime.now().month
     year=datetime.datetime.now().year
     tahunn=int(datetime.datetime.now().year)
     if request.method == "POST":
          bulan = request.POST.get('bulan')
          year  = request.POST.get('tahun')
          month = int(datetime.datetime.strptime(bulan,'%b').month)
          query = Fundmodel.objects.filter(milik_id=request.user.id,Tanggal__month=month,Tanggal__year=year)
          for x in query:
               if x.kategori=="Pengeluaran":
                    pengeluaran=pengeluaran+((-1)*x.Jumlah)
               else:
                    pemasukan=pemasukan+x.Jumlah
          for fund in query:
               labels.append(fund.Tanggal.month)
               data1.append(int(pemasukan))
               data2.append(int(pengeluaran))
          month= calendar.month_name[month]
          saldo = pemasukan+pengeluaran;
          saldo = int(saldo)
          return render(request,'statsss.html',{
                         'labels':labels,
                         'data1':data1,
                         'data2':data2,
                         'month':month,
                         'year':year,
                         'saldo':saldo,
                         })
     query = Fundmodel.objects.filter(milik_id=request.user.id,Tanggal__month=month,Tanggal__year=year)
     for x in query:
          if x.kategori=="Pengeluaran":
               pengeluaran=pengeluaran+((-1)*x.Jumlah)
          else:
               pemasukan=pemasukan+x.Jumlah
     for fund in query:
          labels.append(fund.Tanggal.month)
          data1.append(int(pemasukan))
          data2.append(int(pengeluaran))
     month= calendar.month_name[month]
     saldo = pemasukan+pengeluaran;
     return render(request,'statsss.html',{
          'labels':labels,
          'data1':data1,
          'data2':data2,
          'month':month,
          'year':year,
          'tahunn':tahunn,
          'saldo':saldo,
          
          
     })


