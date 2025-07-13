from django.contrib import admin
from .models import UserInvestment, InvestmentPlan, Wallet, Transaction

# Register your models here.

admin.site.register([UserInvestment, InvestmentPlan, Wallet, Transaction])