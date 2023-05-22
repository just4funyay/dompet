from django.db import models
from django.contrib.auth.models import User

class Fundmodel(models.Model):
    KATEGORI = [('Pendapatan','Pendapatan'),
                ('Pengeluaran','Pengeluaran')]
    kategori = models.TextField(choices=KATEGORI,default='Pendapatan')
    Tanggal = models.DateField()
    Jumlah = models.IntegerField(default=0)
    Deskripsi = models.TextField()
    milik = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table="Laporan"
