from django import forms
from app1.models import Employee
class Forms1(forms.ModelForm):
    #meta : the meta class can be used to defined various things about the models such as the permission database
    class Meta:
        model =  Employee
        fields = '__all__'
