from django import forms  
from django.forms import ModelForm
from .models import Regist  
class NewRegist(forms.ModelForm):  
    class Meta:  
        model = Regist  
        fields = "__all__"  