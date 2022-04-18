from django.db import models

# Create your models here.


class Account(models.Model):
    account_name = models.CharField(max_length=100)
    account_password = models.CharField(max_length=100)
    account_data = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.account_name
