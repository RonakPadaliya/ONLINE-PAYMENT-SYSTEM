from django import forms


class User_info(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    user_name = forms.CharField()
    password = forms.CharField()