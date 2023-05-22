from django.shortcuts import render,redirect
from .forms import fundForm
from .models import Fundmodel
from reglog import views as reglogviews
from home import views as homeviews
import datetime
from django.views import View
import sys
import calendar

            
def fundpage(request):
    fundform = fundForm()
    if request.method == 'POST':
        
        if fundform.is_valid:
                kat = request.POST.get('kate')
                keluar=int(request.POST.get('duid'))
                if kat == 'Pengeluaran':     
                    masuk = Fundmodel.objects.create(
                     kategori=kat,
                     Tanggal=request.POST.get('tangal'),
                     Jumlah=(-1)*keluar,
                     Deskripsi=request.POST.get('desc'),
                     milik_id=request.user.id)
                    masuk.save()
                elif kat=='Pemasukan':
                     masuk = Fundmodel.objects.create(
                     kategori=kat,
                     Tanggal=request.POST.get('tangal'),
                     Jumlah=request.POST.get('duid'),
                     Deskripsi=request.POST.get('desc'),
                     milik_id=request.user.id)
                     masuk.save()
                return redirect(homeviews.Homepage)
    else:
        fundform = fundForm()
    return render(request,'fund.html',{'fundform':fundform})

def Editform(request, fund_id):
     fund = Fundmodel.objects.get(pk=fund_id)
     return render(request,'fund/<int:>')
def stats(request):
     labels=[]
     data1 = []
     data2 = []
     kata2=""
     pengeluaran=0
     pemasukan=0
     month=datetime.datetime.now().month
     year=datetime.datetime.now().year
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
          if pemasukan>pengeluaran:
               kata2="bulan ini pemasukan lebih baik ayo tingkatkan lagi!"
          elif pengeluaran>pemasukan:
               kata2="bulan ini pengeluaran lebih besar dari pemasukan, ayo lebih hemat lagi!"
          else:
               kata2="bulan ini kamu belum input apapun"
          month= calendar.month_name[month]
          return render(request,'stats.html',{
                         'labels':labels,
                         'data1':data1,
                         'data2':data2,
                         'month':month,
                         'year':year,
                         'kata2':kata2})
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
     if pemasukan>pengeluaran:
               kata2="bulan ini pemasukan lebih baik ayo tingkatkan lagi!"
     elif pengeluaran>pemasukan:
               kata2="bulan ini pengeluaran lebih besar dari pemasukan, ayo lebih hemat lagi!"
     else:
          kata2="bulan ini kamu, tidak menginput apapun"
     month= calendar.month_name[month]
     return render(request,'stats.html',{
          'labels':labels,
          'data1':data1,
          'data2':data2,
          'month':month,
          'year':year,
          'kata2':kata2,
          
     })


