from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.core.exceptions import ValidationError
from .models import User as CustomUser

# class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
#     def populate_user(self, request, sociallogin, data):
#         user = super(CustomSocialAccountAdapter,self).populate_user(request,sociallogin,data)
#         phone_number = data.get('phone_number')
#         if phone_number and CustomUser.objects.filter(phone_number=phone_number).exists():
#             raise ValidationError('A user with this phone number already exists')
#         user.phone_number = phone_number
#         return user
        
# user_management/adapter.py


class CustomAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        # Modify reset URL if present in context
        if 'password_reset_url' in context:
            uid = context.get('uid')
            token = context.get('token')
            context['password_reset_url'] = f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_URL}{uid}/{token}"
        super().send_mail(template_prefix, email, context)
