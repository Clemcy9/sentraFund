from django.contrib.auth.backends import ModelBackend
from .models import User, UserProfile


class PhoneNumberBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"Login attempt: username={username}, password={password}")
        user = None
        try:
            # Try as phone number via profile
            user = UserProfile.objects.get(whatsapp_number=username).user
        except UserProfile.DoesNotExist:
            try:
                # Try as email
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None

        if user and user.check_password(password):
            return user
        return None