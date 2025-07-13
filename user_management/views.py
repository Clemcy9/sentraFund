from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from dj_rest_auth.registration.views import VerifyEmailView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404

# takes care of email confirmation for api reg user
class CustomConfirmEmailView(APIView):
    def get(self, request, key):
        try:
            confirmation = EmailConfirmationHMAC.from_key(key)
            if confirmation:
                confirmation.confirm(request)
                return Response({'detail': _('Email confirmed.')}, status=status.HTTP_200_OK)
        except Exception:
            pass

        # Fallback for expired HMAC or invalid key
        confirmation = get_object_or_404(EmailConfirmation, key=key.lower())
        confirmation.confirm(request)
        return Response({'detail': _('Email confirmed.')}, status=status.HTTP_200_OK)
