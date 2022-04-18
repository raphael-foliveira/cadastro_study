from django.shortcuts import redirect, render
from django import urls
from django import views
from . import models
from . import forms

# Create your views here.


class ShowAccountsView(views.View):

    def get(self, request):
        all_accounts = models.Account.objects.all()
        context = {
            "all_accounts": all_accounts,
        }
        return render(request, "account_manager/showaccounts.html", context=context)


class CreateAccountView(views.View):

    def get(self, request):
        form = forms.CreateAccountForm()
        return render(request, "account_manager/createaccount.html", context={"form": form})

    def post(self, request):
        all_accounts = models.Account.objects.all()
        form = forms.CreateAccountForm(request.POST)
        context = {
            "all_accounts": all_accounts,
            "form": form,
        }
        if form.is_valid():
            name = form["account_name"].value()
            password = form["account_password"].value()
            data = form["account_data"].value()
            models.Account.objects.create(
                account_name=name, account_password=password, account_data=data)
            context = {
                "all_accounts": all_accounts,
                "form": form,
            }
            return render(request, "account_manager/showaccounts.html", context=context)


def delete_account(request, account_pk):
    account = models.Account.objects.get(pk=account_pk)
    account.delete()
    return redirect(urls.reverse("account_manager:show_accounts"))
