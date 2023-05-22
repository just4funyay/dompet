from django import forms
from .models import Fundmodel
class fundForm(forms.ModelForm):
    class Meta:
        model = Fundmodel
        fields = ['kategori','Tanggal','Jumlah','Deskripsi']
        
        
        