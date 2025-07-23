from allauth.socialaccount.signals import pre_social_login, social_account_updated
from django.dispatch import receiver
from allauth.account.signals import email_confirmed
from django.db.models.signals import post_save
from django.conf import settings
from django.db import transaction
from django.utils.timezone import now
from datetime import timedelta
from user_management.models import UserProfile
from investment.models import Transaction, UserInvestment,InvestmentPlan


# user-profile related signals
User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
@transaction.atomic
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'userprofile'):
            UserProfile.objects.create(user=instance)

@receiver(email_confirmed)
@transaction.atomic
def handle_email_confirmation(request, email_address, **kwargs):
    user = email_address.user 
    print(f"{user.email} has confirmed their email.")
    if not hasattr(user, "userprofile"):
        UserProfile.objects.create(user=user)


# investment related signals
def default_due_date(ndays):
    return now() + timedelta(days=ndays)

@receiver(post_save, sender= Transaction)
def create_user_investment(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'userinvestment'):
            try:
                investment_plan = InvestmentPlan.objects.get(name = instance.reference_plan)
                UserInvestment.objects.create(user=instance.user, plan=investment_plan, transaction=instance, due_date = default_due_date(investment_plan.duration_days))
            except:
                print('invalid investmentplan choice: probably a withdraw')
