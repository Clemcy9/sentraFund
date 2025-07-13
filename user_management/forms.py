from allauth.account.forms import LoginForm
from allauth.socialaccount.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from .models import User as CustomUser

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].label = 'Phone number or Email'
        self.fields['login'].widget.attrs['placeholder'] = 'Phone number/Email'

# class CustomSignupForm(SignupForm):
#     phone_number = forms.CharField(max_length=15, required=True)

#     def __init__(self, *args, **kwargs):
#         self.sociallogin = kwargs.pop('sociallogin', None)
#         super(CustomSignupForm, self).__init__(*args, **kwargs)
        
#     def clean_phone_number(self):
#         phone_number = self.cleaned_data['phone_number']
#         if CustomUser.objects.filter(phone_number=phone_number).exists():
#             raise ValidationError("A user with this phone number already exists.")
#         return phone_number

#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         user.phone_number = self.cleaned_data['phone_number']
#         user.save()
#         return user