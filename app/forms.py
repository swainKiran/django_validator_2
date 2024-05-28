from django import forms
from app.models import *
from django.core import validators
class StudentForm(forms.ModelForm):
    remail=forms.EmailField()
    class Meta:
        model = Student
        fields = '__all__'
    def clean(self):
        e=self.cleaned_data['semail']
        re=self.cleaned_data['remail']
        if e!=re:
            raise forms.ValidationError('email not matched')    

class GuradianForm(forms.ModelForm):
    mobileno=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    class Meta:
        model = Guradian
        fields = '__all__'