from django import forms



class CrearAuto(forms.Form):
    marca = forms.CharField( max_length= 30)
    modelo = forms.CharField( max_length= 30)