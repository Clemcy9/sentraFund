from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
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
        