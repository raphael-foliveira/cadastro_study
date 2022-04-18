from django.urls import path
from . import views

app_name = 'account_manager'

urlpatterns = [
    path('showaccounts', views.ShowAccountsView.as_view(), name="show_accounts"),
    path('createaccount', views.CreateAccountView.as_view(), name="create_account"),
    path('delete/<account_pk>', views.delete_account, name="delete_account")
]
