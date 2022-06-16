from django import forms


class CreateAccountForm(forms.Form):
    account_name = forms.CharField(max_length=100, label="Name: ")
    account_password = forms.CharField(
        max_length = 100, label="Password: ", widget=forms.PasswordInput())
    account_data = forms.CharField(max_length=200, label="Content: ")
