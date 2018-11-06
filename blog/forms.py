from django import forms

class UserForm(forms.Form):
    your_name = forms.CharField(label='your_name')
    password = forms.CharField(label='password')