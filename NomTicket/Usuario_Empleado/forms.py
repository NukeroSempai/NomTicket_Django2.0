from django import forms
from CORE.models import EMPLEADO

class empleadoForm(forms.ModelForm):
    clave = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = EMPLEADO
        fields = '__all__'
        
class loginEmpForm(forms.ModelForm):
    clave=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = EMPLEADO
        fields = ['rut_emp', 'clave']
    
