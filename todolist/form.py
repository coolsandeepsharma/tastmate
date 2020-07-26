from django import forms
from todolist.models import tasklist

class taskform(forms.ModelForm):
    class Meta:
        model = tasklist
        fields = ['task','done']
