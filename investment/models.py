from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_fullname()} - Balance: {self.balance}"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    # reference = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_fullname()} - {self.transaction_type} - {self.amount} ({self.status})"

class InvestmentPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # e.g. 15.50%
    duration_days = models.IntegerField()  # how long the plan lasts
    minimum_amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.interest_rate}% for {self.duration_days} days"

class UserInvestment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(InvestmentPlan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    payout_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    payout_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name} - ₦{self.amount}"
